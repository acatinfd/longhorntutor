import webapp2
import json
from domain.Order import Order
from handlers.helper.Messages import getAlertMessage

class CreateNewOrder(webapp2.RequestHandler):
    def post(self):
        owner_id = self.request.get('user_id')
        subject = self.request.get('subject')
        title = self.request.get('title')
        comment = self.request.get('comment')
        return_url = self.request.get('return_url')

        order = Order(owner_id=owner_id, subject=subject, title=title, \
                    comment=comment, status_code=1)
        key = order.put()

        self.response.write(json.dumps({'status_code': 0, 'key': key.id()}))
        if return_url:
            self.redirect(getAlertMessage(return_url, "A new post is created!"))
