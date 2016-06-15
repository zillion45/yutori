from base import *

class SignupHandler(BaseHandler):
    def get(self):
        self.render('signup.html', next=self.get_argument('next', '/'))
    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        password_confirm = self.get_argument('password_confirm', '')
        email = self.get_argument('email', '')

        user = User(username=username, password=password, email=email)
        user.save()

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html', next=self.get_argument('next', '/'))
    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')

class LogoutHandler(BaseHandler):
    pass
