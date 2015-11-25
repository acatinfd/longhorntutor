import webapp2
import json
from domain.TutorSubject import TutorSubject

class AddSubject(webapp2.RequestHandler):
    def post(self):
        subject_id = self.request.get('subject_id')
        user_id = self.request.get('user_id')
        intro = self.request.get('intro_text')

        tutorSubject = TutorSubject(user_id=user_id, subject_id=subject_id, intro=intro, rating=0)
        key = tutorSubject.put()

        self.response.write(json.dumps({'status_code': 0, 'key': key.id()}))
