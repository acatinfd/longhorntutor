import webapp2
import json
from domain.UserInfo import UserInfo
from domain.TutorSubject import TutorSubject

class GetUser(webapp2.RequestHandler):
    def get(self):
        user_id = self.request.get('user_id')
        email = self.request.get('email')
        user = UserInfo.query_by_id(user_id)

        if(user is None):
            #create the user
            user = UserInfo(user_id=user_id, name="", email=email, picture=None, tutor_rating=0, intro="")
            key = user.put()
            user = UserInfo.query_by_id(user_id)

        subjects = TutorSubject.query_by_tutor_id(user_id)
        subjects = ', '.join([p.subject for p in subjects])

        self.response.write(json.dumps({'status_code':0, 'user_id': user_id, 'name': user.name,\
         'email': user.email, 'tutor_rating': user.tutor_rating, \
         'intro':user.intro, 'subjects': subjects, \
         'picture': str(user.picture)}))
