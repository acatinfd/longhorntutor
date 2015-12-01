import webapp2
import json
from domain.OrderUser import OrderUser

class GetPendingOrders(webapp2.RequestHandler):
    def get(self):
        user_id = self.request.get('user_id')

        orders = OrderUser.query_by_user_id(user_id)
        if orders is None:
            self.response.write(json.dumps({'status_code': 1}))
        else:
            pendingOrders = [{'order_id': od.order_id} for od in orders if od.status_code == 1]
            self.response.write(json.dumps(pendingOrders))
