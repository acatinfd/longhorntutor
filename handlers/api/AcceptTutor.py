import webapp2
import json

from domain.OrderUser import OrderUser
from domain.Notify import Notify

from handlers.helper.Messages import getInviteURL, getAcceptTutorMessage, getAlertMessage
from handlers.helper.GetPath import GetPath

class AcceptTutor(webapp2.RequestHandler):
    def post(self):
        user_id = self.request.get('user_id') #tutor id
        order_id = self.request.get('order_id')
        return_url = self.request.get('return_url')
        order = OrderUser.query_by_user_and_order(user_id, order_id)
        message = "Accepted tutor!"

        if (order is None or order.status_code != 2):
            self.response.write(json.dumps({'status_code': -1}))
            message = "Request no longer exists."
        else:
            order.status_code = 3 #accept the tutor
            order.put()

            #generate notify
            base = GetPath(self.request.url, self.request.path)
            notify = Notify(from_user="", to_user=user_id, content=getAcceptTutorMessage(), url=getInviteURL(base, order_id), status_code=1)
            notify.put()
            self.response.write(json.dumps({'status_code': 0}))

        if return_url:
            self.redirect(getAlertMessage(return_url, message))
