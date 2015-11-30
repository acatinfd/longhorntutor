from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers
import webapp2

from domain.UserInfo import UserInfo

class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        try:
            upload = self.get_uploads()[0]
            user = users.get_current_user().user_id()
            userinfo = UserInfo.query_by_id(user)

            #delete old photo
            if userinfo.picture:
                blobstore.delete(userinfo.picture)

            userinfo.picture = upload.key()
            userinfo.put()
            self.redirect('/profile')
        except:
            self.error(500)

class ViewPhotoHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, photo_key):
        if not blobstore.get(photo_key):
            self.error(404)
        else:
            self.send_blob(photo_key)
