import webapp2
import json
from domain.OrderUser import OrderUser
from domain.Order import Order
from domain.Notify import Notify

from handlers.helper.Messages import getInviteMessage, getInviteURL
from handlers.helper.GetPath import GetPath

"""
API for adding OrderUser relationship
"""

class InviteTutor(webapp2.RequestHandler):
    def post(self):
        order_id = self.request.get('order_id') #tutor id
        user_id = self.request.get('user_id')
        self_applied = self.request.get('self_applied')

        order = Order.query_by_id(order_id)
        if order is not None:
            #check if already invited
            existOrder = OrderUser.query_by_user_and_order(user_id, order_id)
            if (existOrder is not None):
                self.response.write(json.dumps({'status_code': 0, 'message': 'already exists'}))
                return

            #create an invitation
            invitation = OrderUser(user_id=user_id, order_id=order_id, \
                status_code=1, order_status=order.status_code)
            if (self_applied):
                invitation.status_code=2
            else:
                #generate notify
                base = GetPath(self.request.url, self.request.path)
                notify = Notify(from_user="", to_user=user_id, content=getInviteMessage(order_id), url=getInviteURL(base, order_id), status_code=1)
                notify.put()
            key = invitation.put()
            self.response.write(json.dumps({'status_code': 0, 'key': key.id()}))
        else:
            self.response.write(json.dumps({'status_code': -1}))
