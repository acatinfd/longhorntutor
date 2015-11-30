from google.appengine.ext import ndb

"""
status_code:
    1: open
    0: close
"""

class Notify(ndb.Model):
    from_user = ndb.StringProperty()
    to_user = ndb.StringProperty()
    content = ndb.StringProperty()
    url = ndb.StringProperty()
    status_code = ndb.IntegerProperty()
    create_time = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_by_from_user(cls, from_user):
        return Notify.query(Notify.from_user == from_user)

    @classmethod
    def query_by_to_user(cls, to_user):
        return Notify.query(Notify.to_user == to_user)

    @classmethod
    def query_by_from_and_to_users(cls, from_user, to_user):
        users = Notify.query_by_from_user(from_user)
        for u in users:
            if u.to_user == to_user:
                return u
        return None

    @classmethod
    def query_by_id(cls, notify_id):
        return cls.get_by_id(int(notify_id))
