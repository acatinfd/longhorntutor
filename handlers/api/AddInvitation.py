import webapp2
import time, json
from domain.Invitation import Invitation

class AddInvitation(webapp2.RequestHandler):
    def post(self):
        student_id = self.request.get('student_id')
        tutor_id = self.request.get('tutor_id')
        subject_id = self.request.get('subject_id')

        invitation = Invitation(student_id=student_id, tutor_id=tutor_id, subject_id=subject_id)
        key = invitation.put()

        self.response.write(json.dumps({'status_code': 0, 'key': key.id()}))
