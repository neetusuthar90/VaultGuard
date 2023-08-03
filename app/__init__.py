from flask import Flask
from config import Config
from flask_login import LoginManager, login_manager
from flask import Flask,render_template,flash
from app.extension import db
from app.models.user import User
from app.models.item import Item


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Export db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.forms import bp as forms_bp
    app.register_blueprint(forms_bp)

    return app
