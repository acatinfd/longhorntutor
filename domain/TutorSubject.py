from google.appengine.ext import ndb

class TutorSubject(ndb.Model):
    user_id = ndb.StringProperty()
    subject_id = ndb.StringProperty()
    rating = ndb.FloatProperty()
    intro = ndb.StringProperty()
