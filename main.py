# -*- coding: utf-8 -*-

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

define("port", default=8000, help="run on the given port")

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
        ]
        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), 'tpl'),
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'site_title': u"yutori",
            'debug': True,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
