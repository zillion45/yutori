# -*- coding: utf-8 -*-

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
import motor

from handlers.base import BaseHandler
from handlers.user import SignupHandler, LogoutHandler, LogoutHandler

define("port", default=8000, help="run on the given port")

class HomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('home.html', user=self.current_user)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/signup", SignupHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
        ]
        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), 'tpl'),
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'site_title': u"yutori",
            'xsrf_cookies': True,
            'debug': True
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    db = motor.MotorClient().yutori
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
