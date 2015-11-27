import webapp2
import json

from domain.Order import Order

class GetMyOrders(webapp2.RequestHandler):
    def get(self):
        user_id = self.request.get('user_id')
        orders = Order.query_by_owner_id(user_id)

        if (orders is None or len(orders) == 0):
            self.response.write(json.dumps({'status_code': 1}))
        else:
            myOrders = [{'subject': od.subject, 'title': od.title, \
                        'comment': od.comment, 'status_code': od.status_code,\
                        } for od in orders]
            self.resonse.write(json.dumps(myOrders))
