from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.api.images import get_serving_url

import webapp2
from jinja import JINJA_ENVIRONMENT

import requests

from helper.GetPath import GetPath

class Profile(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            base = GetPath(self.request.url, self.request.path)

            r = requests.get(base + '/api/getuser', params={'user_id': user.user_id(), 'email': user.email()})
            data = r.json()
            data['return_url'] = base + '/profile'
            data['upload_url'] = blobstore.create_upload_url('/upload_photo')

            if data['picture'] is None:
                data['picture'] = '/images/avatar-template.png'
            else:
                data['picture'] = '/view_photo/' + data['picture']

            data['showAlert'] = self.request.get('showAlert')
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
