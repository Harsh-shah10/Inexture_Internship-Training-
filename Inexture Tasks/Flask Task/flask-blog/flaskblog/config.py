import os
from dotenv import load_dotenv


class Config:
    load_dotenv()
    SECRET_KEY=os.environ.get("SECRET_KEY")
    
    # Add Database 
    uri=os.environ.get("DATABASE_URL")
    
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI=uri

    SQLALCHEMY_TRACK_MODIFICATIONS= False 

    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS= True
    MAIL_USERNAME= os.environ.get('EMAIL_USER')
    MAIL_PASSWORD= os.environ.get('EMAIL_PASS')