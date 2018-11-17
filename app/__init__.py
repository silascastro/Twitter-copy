from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
#from flask_mysqldb import MySQL


app = Flask(__name__) #cria app
app.config.from_object('config') #configurações
db = SQLAlchemy(app) #connecta DB
migrate = Migrate(app,db) #migrate

manager = Manager(app)                                                                                                                                                                                                                                                                          
manager.add_command('db',MigrateCommand)

lm = LoginManager()
lm.init_app(app)


from app.models import tables, forms #importa formulários
from app.controllers import default #importa rotas




