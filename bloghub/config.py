import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    database_name = os.environ.get('DATABASE_NAME')
    DB_URI = os.environ.get('DATABASE_URI')
    MONGODB_HOST = DB_URI
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')