from app.extensions.database import db
from flask import Flask
from . import orders
from . import cookies
from app.orders.routes import cookies_blueprint

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')

  register_extensions(app)
  register_blueprints(app)

  return app


def register_blueprints(app: Flask):
  app.register_blueprint(orders.routes.blueprint)
  #app.register_blueprint(cookies.routes.blueprint)
  app.register_blueprint(cookies_blueprint)


def register_extensions(app: Flask):
  from flask_migrate import Migrate

  db.init_app(app)
  migrate = Migrate(app, db, compare_type=True)
  migrate.init_app(app, db, compare_type=True)
  #migrate.init_app(app.orders, db, compare_type=True)



#@app.route('/')
#def homework():
# return render_template('homework.html')

#@app.route('/about')
#def about():
 # works = ["Screaming Face", "Russian sadness", "Trapped inside my mind", "Loving"]
  #return render_template('About.html', works=works)

#@app.route('/works')
#def works():
 # return render_template('Works.html')


#if __name__ == '__main__':
 # app.run(debug=True)

#pp.config.from_object('app.config')
