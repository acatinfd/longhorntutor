import webapp2
import json

from domain.OrderUser import OrderUser

class AcceptTutor(webapp2.RequestHandler):
    def post(self):
        user_id = self.request.get('user_id') #tutor id
        order_id = self.request.get('order_id')
        order = OrderUser.query_by_user_and_order(user_id, order_id)

        if (order is None or order.status_code != 2):
            self.response.write(json.dumps({'status_code': -1}))
            return
        else:
            order.status_code = 3 #accept the tutor
            order.put()
            #TODO: create Notify
            self.response.write(json.dumps({'status_code': 0}))
