from flask import Blueprint

orders_blueprint = Blueprint('orders', __name__)


from . import models, routes
