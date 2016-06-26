import datetime
from mongoengine import *
import bcrypt
from markdown import markdown

class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    email = StringField(required=True)
    avatar = StringField()
    create_time = DateTimeField(auto_now_on_insert=True)

    def check_pwd(self, pwd):
        if bcrypt.hashpw(pwd, self.password) != self.password:
            return False
        else:
            return True

class Post(Document):
    title = StringField(required=True, max_length=100)
    slug = StringField()
    author = ReferenceField(reference_document_type=User)
    body = StringField(required=True)
    tags = ListField(StringField(max_length=30))
    pub_date = DateTimeField(auto_now_on_insert=True)
    comments = ListField(EmbeddedDocumentField(Comment))

class Comment(EmbeddedDocument):
    author = StringField(required=True)
    content = StringField()
