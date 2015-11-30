from google.appengine.api import users
import webapp2
from jinja import JINJA_ENVIRONMENT
from helper.GetPath import GetPath

from domain.OrderUser import OrderUser
from domain.Order import Order

import requests

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            base = GetPath(self.request.url, self.request.path)
            r = requests.get(base + '/api/getmyorders', params={'user_id': user.user_id()})
            orders = r.json()

            r = requests.get(base + '/api/getnewnotify', params={'user_id': user.user_id()})
            notifies = r.json()

            r = requests.get(base + '/api/getpendingorders', params={'user_id': user.user_id()})
            pendingOrders = r.json()
            if len(pendingOrders):
                for p in pendingOrders:
                    r = requests.get(base + '/api/getorderinfo', params={'order_id': p['order_id']})
                    orderInfo = r.json()
                    if len(orderInfo):
                        p['owner_name'] = orderInfo['name']
                        p['subject'] = orderInfo['subject']
                        p['title'] = orderInfo['title']
                        p['comment'] = orderInfo['comment']
                        p['owner_id'] = orderInfo['owner_id']
                    else:
                        pendingOrders.remove(p)
                        
            showAlert = self.request.get('showAlert')
            template_values = {
                'user_id' : user.user_id(),
                'orders': orders,
                'notifies': notifies,
                'pendingOrders': pendingOrders,
                'return_url': base + '/',
                'showAlert': showAlert,
            }

            template = JINJA_ENVIRONMENT.get_template('home.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            template_values = {
                'user' : user,
                'login_logout_url' : url,
                'url_linktext': url_linktext
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))
