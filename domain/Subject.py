from google.appengine.ext import ndb

"""
name: subject name
intro: text that introduce the subject
grade: beginner, intermediate, advanced
"""
class Subject(ndb.Model):
    name = ndb.StringProperty()
    intro = ndb.StringProperty()
    grade = ndb.IntegerProperty()

    @classmethod
    def query_by_id(cls, subject_id):
        return cls.get_by_id(subject_id)
