import webapp2
import json, time
from domain.UserInfo import UserInfo

class GetUser(webapp2.RequestHandler):
    def get(self):
        user_id = self.request.get('user_id')
        user = UserInfo.query_by_id(user_id)

        if(user is None):
            #create the user
            user = UserInfo(user_id=user_id, name="New User", email="", picture=None, tutor_rating=0, intro="")
            key = user.put()
            user = UserInfo.query_by_id(user_id)

        self.response.write(json.dumps({'name': user.name,\
         'email': user.email, 'tutor_rating': user.tutor_rating, 'intro':user.intro}))
