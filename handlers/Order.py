from google.appengine.api import users
import webapp2
import requests
from jinja import JINJA_ENVIRONMENT
from helper.GetPath import GetPath
from helper.PictureURL import getPictureURL

from domain.Order import Order
from domain.OrderUser import OrderUser

class Order(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            order_id = self.request.get('order_id')
            base = GetPath(self.request.url, self.request.path)
            r = requests.get(base + '/api/getorderinfo', params={'order_id': order_id})
            order_info = r.json()

            if order_info:
                order_info['user_id'] = user.user_id()
                order_info['is_applied'] = False
                order_info['hasSelectedTutor'] = False
                order_info['own_the_order'] = False

                exist_order = OrderUser.query_by_user_and_order(user.user_id(), order_id)
                if (exist_order and exist_order.status_code == 2):
                    order_info['is_applied'] = True

                if order_info['selectedTutor']:
                    order_info['selectedTutor']['picture'] = getPictureURL(order_info['selectedTutor']['picture'])
                    order_info['hasSelectedTutor'] = True
                    order_info['own_the_order'] = (order_info['selectedTutor']['user_id'] == user.user_id()) or (user.user_id() == order_info['owner_id'])

                if order_info['candidates']:
                    for p in order_info['candidates']:
                        p['picture'] = getPictureURL(p['picture'])
                        
                order_info['return_url'] = base + '/order?order_id=' + order_id
                order_info['showAlert'] = self.request.get('showAlert')

                template = JINJA_ENVIRONMENT.get_template('order.html')
                self.response.write(template.render(order_info))
            else:
                self.response.write("Error! No such order.")
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
