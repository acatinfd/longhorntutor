
def getInviteMessage():
    return 'You are invited to tutor a new student. Check it out!'

def getInviteURL(base, order_id):
    return base+'/order?order_id='+order_id

def getAcceptCandidateMessage():
    return "A tutor has accepted your request. Check it out!"

def getAcceptTutorMessage():
    return "A student has accepted your request. Check it out!"

def getAlertMessage(return_url, message):
    if '?' in return_url:
        return_url = return_url + '&showAlert=' + message
    else:
        return_url = return_url + '?showAlert=' + message
    return str(return_url)
