import tornado.escape
import tornado.ioloop
import tornado.web

class StatusHandler(tornado.web.RequestHandler):
    def get(self):
        response = {'DgmsInstanceId':  'dgms-service-0000'}
        self.write(response)

application = tornado.web.Application([
    (r"/api/rest/status", StatusHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

