import webapp2

from handlers.MainPage import MainPage
from handlers.api.AddInvitation import AddInvitation
from handlers.api.AddSubject import AddSubject
from handlers.api.UpdateUserInfo import UpdateUserInfo

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api/addInvitation', AddInvitation),
    ('/api/addSubject', AddSubject),
    ('/api/updateUserInfo', UpdateUserInfo),
    ], debug = True)
