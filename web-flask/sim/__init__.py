from sim.mahasiswa.routes import rmahasiswa
from flask import Flask
from sim.extension import db, bcrypt, login_manager
import pymysql
from flask_migrate import Migrate

# kofigurasi db mysql dengan pysmysql
dbuser = "root"
dbpass = ""
dbhost = "localhost"
dbname = "pengaduan"
conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(dbuser, dbpass, dbhost, dbname)

app = Flask('__name__', template_folder='sim/templates',
            static_folder='sim/static')
app.config['SECRET_KEY'] = 'randomak'
# kofigurasi sqlalchemy ke sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sim_pengaduan.db'

# kofigurasi sqlalchemy ke mysql
app.config['SQLALCHEMY_DATABASE_URI'] = conn

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(rmahasiswa)
