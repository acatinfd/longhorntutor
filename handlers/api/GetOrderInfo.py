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
            self.response.write(json.dumps({}))
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
                selectedTutor = requests.get(base + '/api/getuser', params={'user_id': tutors[0]['user_id']}).json()
                selectedTutor['tutor_rating'] = int(selectedTutor['tutor_rating'] + 0.5)
            else:
                for ou in all_tutors:
                    if ou.status_code == 2:
                        p = requests.get(base + '/api/getuser', params={'user_id': ou.user_id}).json()
                        print '\n\n\n info is', p, '\n\n\n'
                        p['tutor_rating'] = int(p['tutor_rating'] + 0.5)
                        candidates.append(p)


            self.response.write(json.dumps({'status_code': 0, 'name':user.name, \
                'owner_id': order.owner_id, 'picture': str(user.picture), \
                'email':user.email, 'tutor_rating':user.tutor_rating, \
                'intro':user.intro, 'subject':order.subject, \
                'title':order.title, 'comment':order.comment, \
                'order_id':order_id, 'candidates': candidates, \
                'selectedTutor':selectedTutor, 'order_status':status}))
