from google.appengine.api import users
import webapp2
from jinja import JINJA_ENVIRONMENT
from helper.GetPath import GetPath

import requests

class Search(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            base = GetPath(self.request.url, self.request.path)
            query = self.request.get('queryTerm')

            r = requests.get(base + '/api/searchuser', params={'query': query})
            searchUsers = r.json()
            for u in searchUsers:
                print u
                if u['picture'] != 'None':
                    u['picture'] = '/view_photo/' + u['picture']
                else:
                    u['picture'] = '/images/avatar-template.png'

            r = requests.get(base + '/api/searchorders', params={'query': query})
            searchResults = r.json()

            showAlert = self.request.get('showAlert')
            template_values = {
                'user_id' : user.user_id(),
                'searchUsers': searchUsers,
                'searchResults': searchResults,
                'return_url': base + '/order?order_id=', #TODO
                'showAlert': showAlert,
            }

            template = JINJA_ENVIRONMENT.get_template('search.html')
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
