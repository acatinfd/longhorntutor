import webapp2
import json
from domain.Order import Order

class CreateNewOrder(webapp2.RequestHandler):
    def post(self):
        owner_id = self.request.get('user_id')
        subject = self.request.get('subject')
        title = self.request.get('title')
        comment = self.request.get('comment')

        order = Order(owner_id=owner_id, subject=subject, title=title, \
                    comment=comment, status_code=1)
        key = order.put()

        self.response.write(json.dumps({'status_code': 0, 'key': key.id()}))
