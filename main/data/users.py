import datetime
import mongoengine

class User(mongoengine.Document):
    created = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField()
    email = mongoengine.StringField(unique=True)
    password = mongoengine.StringField()

    ip_address = mongoengine.StringField()


    meta = {
    'db_alias': 'core',
    'collection': 'users',
    'ordering': ['name']
}

    