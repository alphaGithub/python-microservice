from mongoengine import Document, StringField, DateTimeField,ObjectIdField, MapField

# Connect to MongoDB


# Define a MongoDB model as a Python class
class Events(Document):
    _id = ObjectIdField()
    short_id = StringField(required=True)
    name = StringField(required=True)
    description = StringField(required=True)
    meta_data = MapField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
