
import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # splitting the file name and its extension
    _, f_ext = os.path.splitext(form_picture.filename) 
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_filename)
    
    # for saving the image into a compressed form we will be using Pillow lib
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_filename



def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset request', 
                    sender='harshblog@gmail.com', 
                    recipients=[user.email])
    msg.body = f'''To reset the password, Visit the followinf Link : 
{url_for('users.reset_token',token=token, _external=True)}
'''
    mail.send(msg)

