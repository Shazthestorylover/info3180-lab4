from flask import Flask

# Config Values
UPLOAD_FOLDER = './app/static/uploads/'
USERNAME = 'anonymousUser123'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'randomk&y1234567890'

app = Flask(__name__)
app.config.from_object(__name__)
from app import views
