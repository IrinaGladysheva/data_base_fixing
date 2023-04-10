from flask import Blueprint, render_template
from .models import Works
from app.extensions.database import db


blueprint = Blueprint('orders', __name__)


@blueprint.route('/')
def homework():
  return render_template('homework.html')

@blueprint.route('/about')
def about():
  works = ["Screaming Face", "Russian sadness", "Trapped inside my mind", "Loving"]
  return render_template('About.html', works=works)

@blueprint.route('/all_works')
def all_works():
  all_works = Works.query.all()
  return render_template('Works.html', tmp=all_works)

@blueprint.route('/works/<slug>')
def works(slug):
  works = Works.query.filter_by(slug=slug).first()
  return render_template('show.html', works=works)

