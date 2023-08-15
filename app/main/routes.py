from app.main import bp
from flask import Flask,render_template,flash,session
from flask import request, url_for, redirect, abort
from app.forms.registration import RegistrationForm
from app.forms.login import LoginForm
from app.forms.new_item import ItemForm
from flask_login import login_user, current_user, login_required, logout_user
from app.models.user import User
from app.models.item import Item
from app import db


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/register', methods = ['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if(user is not None):
            flash('Email already exists. Please choose a different email address!!')
            return redirect(url_for('main.register'))
        user = User(username = form.username.data, email = form.email.data, password= form.password1.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('registration.html',form=form)


@bp.route('/login', methods = ['GET','POST'])
def login():

    if session.get('locked'):
        # Handle locked state
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=current_user.email).first()
            if user is not None and user.check_password(form.password.data):
                login_user(user)
                session.pop('locked', None)  # Unlock the session
                next = request.args.get("next")
                return redirect(next or url_for('main.vault'))
            flash('Invalid password.')
        return render_template('login.html', form=form)
    
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('main.vault'))
        flash('Invalid email address or Password.')
    return render_template('login.html', form = form)

@bp.route('/new_item', methods = ['GET','POST'])
def new_item():
    form = ItemForm()
    if form.validate_on_submit():
        # Create a new password entry and associate it with the current user
        item = Item(
            website_name = form.website_name.data,
            username = form.username.data,
            password = form.password.data,
            user = current_user
        )
        db.session.add(item)
        db.session.commit()
        flash('Password saved successfully!', 'success')
        return redirect(url_for('main.vault'))
    user_passwords = Item.query.filter_by(user = current_user).all()
    return render_template('new_item.html', form = form, password = user_passwords)

@bp.route('/vault',methods = ['GET'])
@login_required
def vault():
    user_items = current_user.items
    return render_template('vault.html', user_items=user_items)



@bp.route('/item_details/<int:item_id>')
@login_required
def item_details(item_id):
    item = Item.query.filter_by(id = item_id, user = current_user).first()

    if not item:
        abort(404)
    return render_template('item_details.html', item = item)


@bp.route('/edit_item/<int:item_id>', methods = ['GET','POST'])
@login_required
def edit_item(item_id):
    item = Item.query.filter_by(id=item_id, user = current_user).first()

    if not item:
        abort(404)
    if request.method == 'POST':
        if 'cancel' in request.form:
            return redirect(url_for('main.item_details', item_id=item.id))
        item.website_name = request.form['website_name']
        item.username = request.form['username']
        item.password = request.form['password']
        
        db.session.commit()
        flash('Item edited successfully!','success')
        return redirect(url_for('main.item_details'))

    return render_template('edit_item.html', item = item)


@bp.route('/delete_item/<int:item_id>', methods=['POST'])
@login_required
def delete_item(item_id):
    item = Item.query.filter_by(id=item_id, user=current_user).first()

    if not item:
        abort(404)

    if request.method == 'POST':
        # Delete the item
        db.session.delete(item)
        db.session.commit()
        flash('"{}" was successfully deleted!'.format(item['title']))
        #flash('Item deleted successfully!', 'success')
        return redirect(url_for('main.vault'))

    return render_template('item_details.html', item=item)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/lock')
@login_required
def lock():
    session['locked'] = True
    return redirect(url_for('main.login'))
