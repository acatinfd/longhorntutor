from google.appengine.api import users
import webapp2
import requests
from jinja import JINJA_ENVIRONMENT
from helper.GetPath import GetPath
from helper.PictureURL import getPictureURL

class UserInfo(webapp2.RequestHandler):
    def get(self):
        user_id = self.request.get('user_id')
        if user_id:
            base = GetPath(self.request.url, self.request.path)

            r = requests.get(base + '/api/getuser', params={'user_id': user_id})
            data = r.json()
            data['picture'] = getPictureURL(data['picture'])
            data['tutor_rating'] = int(data['tutor_rating'] + 0.5)
            r = requests.get(base + '/api/getmyorders', params={'user_id': user_id})
            data['orders'] = r.json()
            data['logout_url'] = users.create_logout_url(self.request.uri)
            template = JINJA_ENVIRONMENT.get_template('userinfo.html')
            self.response.write(template.render(data))
        else:
            self.error(500)
