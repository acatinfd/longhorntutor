import webapp2
import json

from domain.Order import Order

class SearchOrders(webapp2.RequestHandler):
    def get(self):
        query = self.request.get('query')
        orders = Order.query_by_subject(query)

        if orders is None:
            self.response.write(json.dumps([]))
        else:
            myOrders = [{'subject': od.subject, 'title': od.title, \
                        'comment': od.comment, 'status_code': od.status_code,\
                        'order_id': od.key.id(),\
                        } for od in orders]
            self.response.write(json.dumps(myOrders))
