import webapp2
import json

from domain.Order import Order
from domain.UserInfo import UserInfo

from handlers.helper.PictureURL import getPictureURL

class SearchOrders(webapp2.RequestHandler):
    def get(self):
        query = self.request.get('query')
        orders = Order.query_by_subject(query)

        if orders is None:
            self.response.write(json.dumps([]))
        else:
            myOrders = []
            for od in orders:
                userinfo = UserInfo.query_by_id(od.owner_id)
                if userinfo:
                    myOrders.append({'subject': od.subject, 'title': od.title, \
                                'comment': od.comment, 'status_code': od.status_code,\
                                'order_id': od.key.id(), 'user_id': od.owner_id, 'name': userinfo.name,\
                                'picture': getPictureURL(str(userinfo.picture))})

            self.response.write(json.dumps(myOrders))
