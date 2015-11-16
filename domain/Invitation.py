from google.appengine.ext import ndb

class Invitation(ndb.Model):
    student_id = ndb.StringProperty()
    tutor_id = ndb.StringProperty()
    subject_id = ndb.StringProperty()
    create_time = ndb.DateTimeProperty(auto_now_add=True)
