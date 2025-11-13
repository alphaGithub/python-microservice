from mongoengine import Document, StringField, IntField, connect

# Connect to MongoDB
connect('mydatabase')

# Define a MongoDB model as a Python class
class User(Document):
    username = StringField(required=True, unique=True, max_length=50)
    email = StringField(required=True)
    age = IntField()

# Example usage: creating a user
user = User(username='johndoe', email='john@example.com', age=30)
user.save()

# Querying
user_from_db = User.objects(username='johndoe').first
