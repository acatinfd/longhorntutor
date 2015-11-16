import webapp2
from jinja import JINJA_ENVIRONMENT

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello world!")
