import webapp2
import json, time
from domain.LonghornUser import LonghornUser

class UpdateUserInfo(webapp2.RequestHandler):
    def post(self):
        user_id = self.request.get('user_id')
        name = self.request.get('name')
        email = self.request.get('email')
        intro = self.request.get('intro_text')

        lhUser = LonghornUser.query_by_id(user_id)
        if(lhUser):
            if(name):
                lhUser.name = name
            if(email):
                lhUser.email = email
            if(intro):
                lhUser.intro = intro
        else:
            lhUser = LonghornUser(user_id=user_id, email=email, name=name, intro=intro, tutor_rating=0, picture=null)

        key = lhUser.put()
        self.response.write(json.dumps({'status_code': 0, 'key': key.id()}))
