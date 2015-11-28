import webapp2
import json, time
from domain.UserInfo import UserInfo

class UpdateUserInfo(webapp2.RequestHandler):
    def post(self):
        user_id = self.request.get('user_id')
        name = self.request.get('name')
        email = self.request.get('email')
        intro = self.request.get('intro_text')

        print '\n\n\n intro is', intro, '\n\n\n'
        user = UserInfo.query_by_id(user_id)
        if(user):
            if(name):
                user.name = name
            if(email):
                user.email = email
            if(intro):
                user.intro = intro
        else:
            user = UserInfo(user_id=user_id, email=email, name=name, intro=intro, tutor_rating=0, picture=None)

        key = user.put()
        self.response.write(json.dumps({'status_code': 0, 'key': key.id()}))
