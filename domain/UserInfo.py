from google.appengine.ext import ndb

class UserInfo(ndb.Model):
    user_id = ndb.StringProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    picture = ndb.BlobProperty()
    tutor_rating = ndb.FloatProperty()
    intro = ndb.StringProperty()
    join_time = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_by_id(cls, user_id):
        return UserInfo.query(UserInfo.user_id == user_id)
