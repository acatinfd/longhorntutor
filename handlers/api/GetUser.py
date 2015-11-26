import webapp2
import json, time
from domain.LonghornUser import LonghornUser

class GetUser(webapp2.RequestHandler):
    def get(self):
        user_id = self.request.get('user_id')
        lhUser = LonghornUser.query_by_id(user_id)

        if(lhUser is None):
            #create the user
            lhUser = LonghornUser(user_id=user_id, name="", email="", picture=null, tutor_rating=0, intro="")
            key = lhUser.put()

        self.response.write(json.dumps({'name': lhUser.name,\
         'email': lhUser.email, 'tutor_rating': lhUser.tutor_rating, 'intro':lhUser.intro}))
         
