from webob import Request


class Middleware:

    def __init__(self, app):
        self.app = app

    def add(self, middleware_cls):
        self.app = middleware_cls(self.app)

    def process_request(self, req):
        pass

    def process_response(self, req, resp):
        pass

    def handle_request(self, req):
        self.process_request(req)
        response = self.app.handle_request(req)
        self.process_response(req, response)
        return response

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.app.handle_request(request)
        return response(environ, start_response)
