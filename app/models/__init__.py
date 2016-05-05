from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    update_date = ndb.DateTimeProperty(auto_now=True)
