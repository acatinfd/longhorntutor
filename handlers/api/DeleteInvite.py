import webapp2
import json
from domain.OrderUser import OrderUser
from domain.Order import Order

"""
API for adding OrderUser relationship
"""

class DeleteInvite(webapp2.RequestHandler):
    def post(self):
        order_id = self.request.get('order_id') #tutor id
        user_id = self.request.get('user_id')

        order = Order.query_by_id(order_id)
        if order is not None:
            #check if already invited
            existOrder = OrderUser.query_by_user_and_order(user_id, order_id)
            if (existOrder is not None):
                existOrder.key.delete()
                self.response.write(json.dumps({'status_code': 0}))
                return

        self.response.write(json.dumps({'status_code': 1}))
