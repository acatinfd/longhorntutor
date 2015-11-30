import webapp2
import json

from domain.UserInfo import UserInfo
from domain.TutorSubject import TutorSubject

class SearchUser(webapp2.RequestHandler):
    def get(self):
        query = self.request.get('query')
        users = UserInfo.query_by_keyword(query)

        tutorsubjects = TutorSubject.query_by_subject(query)
        for t in tutorsubjects:
            tutor = UserInfo.query_by_id(t.user_id)
            if not tutor in users:
                users.append(tutor)

        if users is not None:
            usersFound = [ {'user_id': u.user_id, 'name': u.name, 'picture': str(u.picture), \
                        'email': u.email, 'intro': u.intro, 'tutor_rating': int(u.tutor_rating + 0.5)} \
                        for u in users]
            self.response.write(json.dumps(usersFound))
