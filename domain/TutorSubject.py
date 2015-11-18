from google.appengine.ext import ndb

class TutorSubject(ndb.Model):
    user_id = ndb.StringProperty()
    subject_id = ndb.StringProperty()
    rating = ndb.FloatProperty()
    intro = ndb.StringProperty()

    @classmethod
    def query_by_tutor_id(cls, tutor_id):
        return TutorSubject.query(TutorSubject.user_id == tutor_id)

    @classmethod
    def query_by_subject_id(cls, subject_id):
        return TutorSubject.query(TutorSubject.subject_id == subject_id)

    
