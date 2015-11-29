from google.appengine.ext import ndb

"""
status_code:
    1: open
    0: close
"""


class Order(ndb.Model):
    owner_id = ndb.StringProperty()
    subject = ndb.StringProperty()
    title = ndb.StringProperty()
    comment = ndb.StringProperty()
    status_code = ndb.IntegerProperty()
    create_time = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_by_owner_id(cls, student_id):
        return Order.query(Order.owner_id == student_id)

    @classmethod
    def query_by_id(cls, order_id):
        return cls.get_by_id(int(order_id))
