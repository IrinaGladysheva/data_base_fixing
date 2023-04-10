from flask import Blueprint
from . import routes

cookies_blueprint = Blueprint('cookies', __name__)

from app.extensions.database import db
from .models import Cookie