from google.appengine.ext import ndb

class Subject(ndb.Model):
    name = ndb.StringProperty()
    intro = ndb.StringProperty()
    grade = ndb.IntegerProperty()
