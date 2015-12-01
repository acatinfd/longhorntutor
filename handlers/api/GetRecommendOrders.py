import webapp2
import json, random
from domain.Order import Order
from domain.TutorSubject import TutorSubject
from domain.UserInfo import UserInfo

from handlers.helper.PictureURL import getPictureURL

class GetRecommendOrders(webapp2.RequestHandler):
    def get(self):
        user_id = self.request.get('user_id')
        orders = []

        if user_id is not None:
            #each subject pick up 5 orders. then randomly choose 5 from the set
            subjects = TutorSubject.query_by_tutor_id(user_id)
            for s in subjects:
                ods = Order.query_by_subject(str(s.subject))
                for od in ods:
                    userinfo = UserInfo.query_by_id(od.owner_id)
                    if userinfo:
                        orders.append({'subject': od.subject, 'title': od.title, \
                                    'comment': od.comment, 'status_code': od.status_code,\
                                    'order_id': od.key.id(), 'user_id': od.owner_id, 'name': userinfo.name,\
                                    'picture': getPictureURL(str(userinfo.picture))})
        if orders == []:
            #randomly pick up
            ods = Order.query()
            for od in ods:
                userinfo = UserInfo.query_by_id(od.owner_id)
                if userinfo:
                    orders.append({'subject': od.subject, 'title': od.title, \
                                'comment': od.comment, 'status_code': od.status_code,\
                                'order_id': od.key.id(), 'user_id': od.owner_id, 'name': userinfo.name,\
                                'picture': getPictureURL(str(userinfo.picture))})
        random.shuffle(orders)
        recommendOrders = orders[:5]
        self.response.write(json.dumps(recommendOrders))
