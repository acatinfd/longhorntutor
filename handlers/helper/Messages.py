
def getInviteMessage(order_id):
    return 'You are invited to tutor a new student. Check it out!'

def getInviteURL(base, order_id):
    return base+'/order?order_id='+order_id
