from app import PyTezApp
from middleware import Middleware

app = PyTezApp()

# def app(environ, start_response):
#     print(environ)
#     status = "200 OK"
#     headers = [("Content-type", "text/plain")]
#     start_response(status, headers)
#     return [b"Hello world"]


@app.route('/home')
def home(request, response):
    response.text = "Hello from home page"


@app.route('/about')
def about(request, response):
    response.text = "Hello from about page"


@app.route('/hello/{name}')
def greeting(request, response, name):
    response.text = f"Hello from {name}"


@app.route('/books')
class Books:

    def get(self, request, response):
        response.text = "Books page"

    def post(self, request, response):
        response.text = "Endpoint to create a book"


def new_handler(req, resp):
    resp.text = 'from new handler'


app.add_route('/new-handler', new_handler)


@app.route('/template')
def template_handler(req, resp):
    resp.body = app.template(
        "home.html",
        context={"new_title": "Best title", "new_body": "best title"}
    )


def on_exception(req, resp, exe):
    resp.text = 'something bad happened'


app.add_exception_handler(on_exception)


@app.route('/exception')
def exception_throwing_handler(req, resp):
    raise AttributeError('some exception')


class LoggingMiddleware(Middleware):

    def process_request(self, req):
        print("request is being called", req.url)

    def process_response(self, req, resp):
        print("response has been generated", req.url)


app.add_middleware(LoggingMiddleware)
