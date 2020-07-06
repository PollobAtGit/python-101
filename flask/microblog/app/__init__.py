from flask import Flask

# __name__ returns module name. not source path
flask_app = Flask(__name__)

from app import routes
