from google.appengine.ext import ndb

class Order(ndb.Model):
    student_id = ndb.StringProperty()
    tutor_id = ndb.StringProperty()
    subject_id = ndb.StringProperty()
    tutor_rating = ndb.IntegerProperty()
    stu_rating = ndb.IntegerProperty()
    tutor_comment = ndb.StringProperty()
    stu_comment = ndb.StringProperty()
    create_time = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_by_student_id(cls, student_id):
        return Order.query(Order.student_id == student_id)

    @classmethod
    def query_by_tutor_id(cls, tutor_id):
        return Order.query(Order.tutor_id == tutor_id)
