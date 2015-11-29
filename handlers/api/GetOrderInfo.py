import webapp2
import json
from domain.Order import Order
from domain.UserInfo import UserInfo
from domain.OrderUser import OrderUser
from handlers.helper.GetPath import GetPath
import requests

class GetOrderInfo(webapp2.RequestHandler):
    def get(self):
        order_id = self.request.get('order_id')
        order = Order.query_by_id(order_id)

        if (order is None):
            self.response.write(json.dumps({'status_code': 1}))
        else:
            user = UserInfo.query_by_id(order.owner_id)
            status = "open"
            if (order.status_code == 0):
                status = "close"

            base = GetPath(self.request.url, self.request.path)

            #check if a tutor is selected
            candidates = []
            selectedTutor = {}

            all_tutors = OrderUser.query_by_order_id(order_id)
            tutors = [ {'user_id':ou.user_id } for ou in all_tutors if ou.status_code == 3]

            if len(tutors):
                selectedTutor['user_id'] = tutors[0]['user_id']
                r = requests.get(base + '/api/getuser', params={'user_id': selectedTutor['user_id']}).json()
                selectedTutor['name'] = r['name']
                selectedTutor['tutor_rating'] = int(r['tutor_rating'] + 0.5)
                selectedTutor['intro'] = r['intro']
            else:
                candidates = [ {'user_id':ou.user_id } for ou in all_tutors if ou.status_code == 2]
                for p in candidates:
                    r = requests.get(base + '/api/getuser', params={'user_id': p['user_id']}).json()
                    p['name'] = r['name']
                    p['tutor_rating'] = int(r['tutor_rating'] + 0.5)
                    p['intro'] = r['intro']

            self.response.write(json.dumps({'status_code': 0, 'name':user.name, 'owner_id': order.owner_id, \
                'email':user.email, 'tutor_rating':user.tutor_rating, \
                'intro':user.intro, 'subject':order.subject, \
                'title':order.title, 'comment':order.comment, \
                'order_id':order_id, 'candidates': candidates, \
                'selectedTutor':selectedTutor, 'status_code':status}))
