import webapp2
import json, time

from domain.UserInfo import UserInfo
from domain.TutorSubject import TutorSubject
from handlers.helper.Messages import getAlertMessage

class UpdateUserInfo(webapp2.RequestHandler):
    def post(self):
        user_id = self.request.get('user_id')
        name = self.request.get('name')
        subjects = self.request.get('subjects')
        intro = self.request.get('intro_text')
        return_url = self.request.get('return_url')

        user = UserInfo.query_by_id(user_id)
        if(user):
            if(name and user.name != name):
                user.name = name
            if(intro and user.intro != intro):
                user.intro = intro
            if(subjects):
                old_subjects = TutorSubject.query_by_tutor_id(user_id)
                old_subjects = [p.subject for p in old_subjects]
                cur_subjects = subjects.split(',')
                cur_subjects = [p.strip() for p in cur_subjects]

                for p in cur_subjects:
                    if p not in old_subjects:
                        new_subject = TutorSubject(user_id=user_id, subject=p, rating=4.0, order_count=0, intro="")
                        new_subject.put()

                for p in old_subjects:
                    if p not in cur_subjects:
                        s = TutorSubject.query_by_tutor_and_subject(user_id, p)
                        if (s is not None):
                            s.key.delete()
        else:
            user = UserInfo(user_id=user_id, email=email, name=name, intro=intro, tutor_rating=0, picture=None)

        key = user.put()
        self.response.write(json.dumps({'status_code': 0, 'key': key.id()}))
        if return_url:
            self.redirect(getAlertMessage(return_url, "Profile is saved!"))
