from app_module import flask_app 

@flask_app.route("/")
@flask_app.route("/index")

def index():
    return "hello from flask app"

