import webapp2
import json
from domain.Order import Order
from domain.UserInfo import UserInfo

class GetOrderInfo(webapp2.RequestHandler):
    def get(self):
        order_id = self.request.get('order_id')
        order = Order.query_by_id(order_id)

        if (order is None):
            self.response.write(json.dumps({'status_code': 1}))
        else:
            user = UserInfo.query_by_id(order.owner_id)
            status = "open"
            if (order.status_code == 0):
                status = "close"

            self.response.write(json.dumps({'status_code': 0, 'name':user.name,\
                'email':user.email, 'tutor_rating':user.tutor_rating, \
                'intro':user.intro, 'subject':order.subject, \
                'title':order.title, 'comment':order.comment, \
                'status_code':status}))
