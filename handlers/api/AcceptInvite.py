import webapp2
import json

from domain.OrderUser import OrderUser
from domain.Order import Order
from domain.Notify import Notify

from handlers.helper.Messages import getInviteURL, getAcceptCandidateMessage, getAlertMessage
from handlers.helper.GetPath import GetPath

class AcceptInvite(webapp2.RequestHandler):
    def post(self):
        user_id = self.request.get('user_id')
        order_id = self.request.get('order_id')
        return_url = self.request.get('return_url')
        message = "Accepted invitation!"

        order = OrderUser.query_by_user_and_order(user_id, order_id)

        if (order is None or order.status_code != 1):
            self.response.write(json.dumps({'status_code': -1}))
            message = "Request no longer exists."
        else:
            order.status_code = 2 #accept to be a candidate
            order.put()

            #generate notify
            order = Order.query_by_id(order_id)
            base = GetPath(self.request.url, self.request.path)
            notify = Notify(from_user="", to_user=order.owner_id, content=getAcceptCandidateMessage(), url=getInviteURL(base, order_id), status_code=1)
            notify.put()

            self.response.write(json.dumps({'status_code': 0}))

        if return_url:
            self.redirect(getAlertMessage(return_url, message))
