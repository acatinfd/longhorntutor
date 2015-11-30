import webapp2

from handlers.MainPage import MainPage
from handlers.Order import Order
from handlers.Profile import Profile
from handlers.Search import Search

from handlers.api.AcceptInvite import AcceptInvite
from handlers.api.AcceptTutor import AcceptTutor
from handlers.api.CreateNewOrder import CreateNewOrder
from handlers.api.DeleteInvite import DeleteInvite
from handlers.api.DismissNotify import DismissNotify
from handlers.api.GetAllUsers import GetAllUsers
from handlers.api.GetMyOrders import GetMyOrders
from handlers.api.GetNewNotify import GetNewNotify
from handlers.api.GetOrderInfo import GetOrderInfo
from handlers.api.GetPendingOrders import GetPendingOrders
from handlers.api.GetUser import GetUser
from handlers.api.InviteTutor import InviteTutor
from handlers.api.SearchOrders import SearchOrders
from handlers.api.SearchUser import SearchUser
from handlers.api.UpdateUserInfo import UpdateUserInfo
from handlers.api.UploadPhoto import *

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/order', Order),
    ('/profile', Profile),
    ('/search', Search),
    ('/api/acceptinvite', AcceptInvite),
    ('/api/accepttutor', AcceptTutor),
    ('/api/createneworder', CreateNewOrder),
    ('/api/deleteinvite', DeleteInvite),
    ('/api/dismissnotify', DismissNotify),
    ('/api/getallusers', GetAllUsers),
    ('/api/getmyorders', GetMyOrders),
    ('/api/getnewnotify', GetNewNotify),
    ('/api/getorderinfo', GetOrderInfo),
    ('/api/getpendingorders', GetPendingOrders),
    ('/api/getuser', GetUser),
    ('/api/invitetutor', InviteTutor),
    ('/api/searchorders', SearchOrders),
    ('/api/searchuser', SearchUser),
    ('/api/updateuserinfo', UpdateUserInfo),
    ('/upload_photo', PhotoUploadHandler),
    ('/view_photo/([^/]+)?', ViewPhotoHandler),
    ], debug = True)
