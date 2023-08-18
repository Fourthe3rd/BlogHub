from datetime import datetime
from bson import ObjectId
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from bloghub import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()




class User(db.Document, UserMixin):
    username = db.StringField(max_length=20, unique=True, required=True)
    email = db.StringField(max_length=120, unique=True, required=True)
    image_file = db.StringField(default='default.jpg')
    password = db.StringField(max_length=60, required=True)
    posts = db.ListField(db.ReferenceField('Post'))


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': str(self.id)}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.objects(id=ObjectId(user_id)).first()

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Document):
    title = db.StringField(max_length=100, required=True)
    date_posted = db.DateTimeField(required=True, default=datetime.utcnow)
    content = db.StringField(required=True)
    author = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)
#    user_id = db.StringField(required=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    