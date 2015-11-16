import webapp2

from handlers.MainPage import MainPage

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ], debug = True)
