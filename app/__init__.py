from flask import Flask

# Config Values
UPLOAD_FOLDER = './app/static/uploads/'
USERNAME = 'noOneKnowsMe'
PASSWORD = 's$cret_Password'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'my_S&cr&t_K&y_u0123456789'

app = Flask(__name__)
app.config.from_object(__name__)
from app import views
