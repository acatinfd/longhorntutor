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
        return UserInfo.query(UserInfo.user_id == user_id).get()

    @classmethod
    def query_by_keyword(cls, text):
        r = []
        if len(text.strip()) == 0:
            return r

        searchTerm = text.lower()
        for user in UserInfo.query():
            if searchTerm in [user.name.lower(), user.email.lower(), user.intro.lower()]:
                r.append(user)
        return r
