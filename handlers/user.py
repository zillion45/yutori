import bcrypt
from handlers.base import BaseHandler

class SignupHandler(BaseHandler):
    def get(self):
        self.render('signup.html', next=self.get_argument('next', '/'))
    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        password_confirm = self.get_argument('password_confirm', '')
        email = self.get_argument('email', '')
        password = bcrypt.hashpw(password, bcrypt.gensalt())

        user = User(username=username, password=password, email=email)
        user.save()
        self.set_secure_cookie('user')

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html', next=self.get_argument('next', '/'))
    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        password = bcrypt.hashpw(password, bcrypt.gensalt())

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect(self.get_argument('next', '/'))
