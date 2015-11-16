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
