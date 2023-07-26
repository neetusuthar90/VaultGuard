from flask import Blueprint

bp = Blueprint('forms', __name__)

from app.forms import login
from app.forms import regestration

