from flaskblog import db,login_manager
from flask import current_app
from datetime import datetime

from flask_login import UserMixin

# for password reset token generation
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


# creating a decorator to make loader to make login_manager work
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# creating models for db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # In relationship we reference the Class name
    posts = db.relationship('Post',backref='author',lazy=True)

    # for generating the token for forgot pass
    def get_reset_token(self, expires_sec=180  ):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8') 

    # for verifying and reset the token
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    
    # In foreign key we reference the table name, Column name
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
