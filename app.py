#https://flask-admin.readthedocs.io/en/latest/introduction/#working-with-the-built-in-templates

from flask import Flask
from flask_admin import Admin
### conda install -c anaconda werkzeug=0.16.1
from werkzeug.utils import cached_property
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.babelex import Babel
from flask_admin import BaseView, expose

# Internacionalizacion i18n
from flask_babelex import Babel
from flask import request
#from flask.ext.babelex import Babel


app = Flask(__name__)
babel = Babel(app)

app.config['SECRET_KEY']              = 'secreta'
app.config['FLASK_ADMIN_SWATCH']      = 'Slate' # 'darkly'  # set optional bootswatch theme
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crud/flask_admin_poc/admin.db' #C:\tmp\crud\last


db = SQLAlchemy(app)

# Definicion del Lenguage a usar
@babel.localeselector
def get_locale():
    return 'es'

class contactos(db.Model):
    __tablename__ = 'contact'
    contact_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name  = db.Column(db.String(30))
    email      = db.Column(db.String(30))
    phone      = db.Column(db.String(12))

class OtraView(BaseView):
    @expose('/')
    def index(self):
        return 'Hola POC!'

admin = Admin(app, name='POC | Flask-Admin', template_mode='bootstrap3')
admin.add_view(ModelView(contactos, db.session))
admin.add_view(OtraView(name='Otro'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True, port=5001)