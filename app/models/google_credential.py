from google.appengine.ext import ndb

from models import BaseModel


class GoogleCredential(BaseModel):
    credential = ndb.JsonProperty(required=True)
    google_id = ndb.StringProperty()
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    picture = ndb.StringProperty()
