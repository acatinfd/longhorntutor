import webapp2
import json
from domain.UserInfo import UserInfo

class GetAllUsers(webapp2.RequestHandler):
    def get(self):
        users = UserInfo.query()
        users = [u.name for u in users if u.name]

        self.response.write(json.dumps({'all_users':users}))
