import webapp2
import json
from domain.OrderUser import OrderUser
from domain.Order import Order

from handlers.helper.Messages import getAlertMessage

"""
API for adding OrderUser relationship
"""

class DeleteInvite(webapp2.RequestHandler):
    def post(self):
        order_id = self.request.get('order_id') #tutor id
        user_id = self.request.get('user_id')
        return_url = self.request.get('return_url')
        message = "Application deleted!"

        order = Order.query_by_id(order_id)
        if order is not None:
            #check if already invited
            existOrder = OrderUser.query_by_user_and_order(user_id, order_id)
            if existOrder is not None:
                existOrder.key.delete()
                self.response.write(json.dumps({'status_code': 0}))
        else:
            self.response.write(json.dumps({'status_code': 1}))
            message = "No such application!"

        if return_url:
            self.redirect(getAlertMessage(return_url, message))
