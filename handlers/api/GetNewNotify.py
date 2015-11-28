import webapp2
import json

from domain.Notify import Notify

class GetNewNotify(webapp2.RequestHandler):
    def get(self):
        to_user = self.request.get('user_id')
        notifys = Notify.query_by_to_user(to_user)

        if (notifys is not None and len(notifys) != 0):
            newNotifys = [ {'from_user': no.from_user, 'content': no.content, \
                            'create_time': no.create_time, 'notify_id': no.key.id()} for no in notifys if no.status_code == 1]
            self.response.write(json.dumps({'new_notifys': newNotifys}))
        else:
            self.response.write(json.dumps({'new_notifys': []}))
