from google.appengine.ext import ndb

"""
status_code:
    1: request
    2: candidate
    3: accept
    0: owner
order_status:
    1: open
    0: close
"""

class OrderUser(ndb.Model):
    order_id = ndb.StringProperty()
    user_id = ndb.StringProperty()
    status_code = ndb.IntegerProperty()
    order_status = ndb.IntegerProperty()
    create_time = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_by_user_id(cls, user_id):
        return OrderUser.query(OrderUser.user_id == user_id)

    @classmethod
    def query_by_order_id(cls, order_id):
        return OrderUser.query(OrderUser.order_id == order_id)

    @classmethod
    def query_by_user_and_order(cls, user_id, order_id):
        orders = OrderUser.query_by_order_id(order_id)

        if (orders is not None):
            for od in orders:
                if od.user_id == user_id:
                    return od
        return None
