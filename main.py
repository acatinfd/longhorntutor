import webapp2

from handlers.MainPage import MainPage
from handlers.api.AcceptInvite import AcceptInvite
from handlers.api.AcceptTutor import AcceptTutor
from handlers.api.CreateNewOrder import CreateNewOrder
from handlers.api.DismissNotify import DismissNotify
from handlers.api.GetMyOrders import GetMyOrders
from handlers.api.GetNewNotify import GetNewNotify
from handlers.api.GetOrderInfo import GetOrderInfo
from handlers.api.GetPendingOrders import GetPendingOrders
from handlers.api.GetUser import GetUser
from handlers.api.InviteTutor import InviteTutor
from handlers.api.SearchUser import SearchUser
from handlers.api.UpdateUserInfo import UpdateUserInfo

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api/acceptInvite', AcceptInvite),
    ('/api/acceptTutor', AcceptTutor),
    ('/api/createNewOrder', CreateNewOrder),
    ('/api/dissmissNotify', DismissNotify),
    ('/api/getMyOrders', GetMyOrders),
    ], debug = True)
