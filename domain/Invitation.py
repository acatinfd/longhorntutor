from google.appengine.ext import ndb

class Invitation(ndb.Model):
    student_id = ndb.StringProperty()
    tutor_id = ndb.StringProperty()
    subject_id = ndb.StringProperty()
    create_time = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_by_student_id(cls, student_id):
        return Invitation.query(Invitation.student_id == student_id)

    @classmethod
    def query_by_tutor_id(cls, tutor_id):
        return Invitation.query(Invitation.tutor_id == tutor_id)
