import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager

from flask_bcrypt import Bcrypt

from flask_mail import Mail

from flaskblog.config import Config


# initialize the database 
db = SQLAlchemy()

# initialize the bcrypt
bcrypt = Bcrypt()

# initialize the LoginManager
login_manager = LoginManager()
 
# @login_required : user must be login to access some web-page
login_manager.login_view='users.login'

# for changing the message design @login_required pass 'info' bootstrap class
login_manager.login_message_category='info'


mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    Migrate(app,db)

    # importing blue-prints from all the pkg we created
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
 
    # registering the blueprint after importing the blueprint
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    return app