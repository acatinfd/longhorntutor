import webapp2
import time, json
from domain.OrderUser import OrderUser
from domain.Order import Order

"""
API for adding OrderUser relationship
"""

class InviteTutor(webapp2.RequestHandler):
    def post(self):
        order_id = self.request.get('order_id')
        user_id = self.request.get('user_id')

        order = Order.query_by_id(order_id)
        if order is not None:
            invitation = OrderUser(user_id=user_id, order_id=order_id, \
                status_code=1, order_status=order.status_code)
            key = invitation.put()
            self.response.write(json.dumps({'status_code': 0, 'key': key.id()}))
        else
            self.response.write(json.dumps({'status_code': -1}))
