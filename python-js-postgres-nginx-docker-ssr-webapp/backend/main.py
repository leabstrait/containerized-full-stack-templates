# handles requests like GET and POST
import tornado.web
import tornado.ioloop

import json
import os
import sys


# Simple request handlers


## This is a GET request handler that will write a simple response to the client
class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, world</h1>")


## This is a GET request handler that will render a template to the client
class renderTemplateRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html")


# Request handlers with parameters


## Query Parameter request handler
class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        number = self.get_argument("number")
        if not number.isdigit():
            self.write("<h1>Please enter a valid number</h1>")
            return
        if int(number) % 2 == 0:
            self.write(f"<h1>The number {number} is even</h1>")
        else:
            self.write(f"<h1>The number {number} is odd</h1>")


## Resource Parameter request handler
class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, student_name, course_id):
        self.write(
            f"Welcome to the course, {student_name}!<br>The course you are viewing is {course_id}"
        )


## This is a GET request handler that will read a file and respond with JSON to the client
class jsonRequestHandler(tornado.web.RequestHandler):
    def get(self):
        with open("animal.txt", "r") as f:
            data = f.read().splitlines()
        self.write(json.dumps(data))

    def post(self):
        animal = self.get_argument("animal")
        with open("animal.txt", "a") as f:
            f.write("\n" + animal)
        self.write(json.dumps({"message": "Animal added successfully"}))


# This is a request handler that will upload a file (POST) to the server and also retrieve it (GET)
class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/images/index.html")

    def post(self):
        files = self.request.files["imageFile"]

        for f in files:
            with open(f"images/imagestore/{f.filename}", "wb") as fp:
                fp.write(f.body)
            self.write(f"http://localhost:8888/img/{f.filename}")


## This is a GET request handler that will identify the processid of the server
class identifyRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, world</h1>")
        self.write(f"Served from {os.getpid()}")


if __name__ == "__main__":
    app = tornado.web.Application(
        [
            (r"/", basicRequestHandler),
            (r"/identify", identifyRequestHandler),
            (r"/animal", renderTemplateRequestHandler),
            (r"/animal/json", jsonRequestHandler),
            (r"/isEven", queryParamRequestHandler),
            (
                r"/students/([a-z]+)/([0-9]+)",  # regular expression to match the resource parameters based on the path. (regex101.com)
                resourceParamRequestHandler,
            ),
            (r"/img/upload", uploadHandler),
            (
                r"/img/(.*)",
                tornado.web.StaticFileHandler,
                {"path": "assets/imagestore"},
            ),
        ]
    )

    port = 8000

    if sys.argv.__len__() > 1:
        port = sys.argv[1]

    app.listen(port)
    print(f"Application is ready and listening on port {port}...")

    tornado.ioloop.IOLoop.current().start()
