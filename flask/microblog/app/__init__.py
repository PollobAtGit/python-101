from flask import Flask
from config import Config

# __name__ returns module name. not source path
flask_app = Flask(__name__)

# [app].config.from_object(...) gets the application configurations from the class passed as argument
flask_app.config.from_object(Config)

from app import routes
