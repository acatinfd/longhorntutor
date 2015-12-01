from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.api.images import get_serving_url

import webapp2
import requests
from jinja import JINJA_ENVIRONMENT
from helper.GetPath import GetPath
from helper.PictureURL import getPictureURL

class Profile(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            base = GetPath(self.request.url, self.request.path)

            r = requests.get(base + '/api/getuser', params={'user_id': user.user_id(), 'email': user.email()})
            data = r.json()
            data['return_url'] = base + '/profile'
            data['upload_url'] = blobstore.create_upload_url('/api/updateuserinfo')

            data['picture'] = getPictureURL(data['picture'])

            data['showAlert'] = self.request.get('showAlert')
            data['logout_url'] = users.create_logout_url(self.request.uri)
            template = JINJA_ENVIRONMENT.get_template('profile.html')
            self.response.write(template.render(data))
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
