import webapp2
import json

from domain.Notify import Notify

class DismissNotify(webapp2.RequestHandler):
    def post(self):
        notify_id = self.request.get('notify_id')
        notify = Notify.query_by_id(notify_id)

        if (notify is not None and notify.status_code == 1):
            notify.status_code = 0
            notify.put()
        self.response.write(json.dumps({'status_code': 0}))
