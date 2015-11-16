from google.appengine.ext import ndb

class LonghornUser(ndb.Model):
    user_id = ndb.StringProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    picture = ndb.BlobProperty()
    tutor_rating = ndb.FloatProperty()
    stu_rating = ndb.FloatProperty()
    intro = ndb.StringProperty()
    join_time = ndb.DateTimeProperty(auto_now_add=True)
