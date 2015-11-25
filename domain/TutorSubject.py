from google.appengine.ext import ndb

"""
Define the relationship that a tutor tutors a subject
user_id: tutor's user_id
subject_id: id of that subject
rating: performance of the tutor in thi subject
intro: personal intro of experience from the tutor
"""

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
