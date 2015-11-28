import webapp2
import json

from domain.UserInfo import UserInfo

class SearchUser(webapp2.RequestHandler):
    def get(self):
        query = self.request.get('query')
        users = UserInfo.query_by_keyword(query)

        if (users is not None and len(users) != 0):
            usersFound = [ {'user_id': u.user_id, 'name': u.name, \
                        'email': u.email, 'intro': u.intro, 'tutor_rating': u.tutor_rating} \
                        for u in users]
            self.response.write(json.dumps({'users': usersFound}))
