from flask_sqlalchemy import SQLAlchemy

# Config Values
UPLOAD_FOLDER = './app/static/uploads/'


# Secret Key
SECRET_KEY = 'INFO3180$3cretkey'

user = 'Shaz'
password = 'I_am_an_exceptional_programmer'
database = 'INFO3180_Project01'
default = "postgresql://%s:%s@localhost/%s" % (user,password,database) 
heruko = 'postgresql://emgxrvvcxwkegj:b88d1a34cd8337edfaf89daf766753b402da35f0296f16e66863b063a2f6479b@ec2-3-234-169-147.compute-1.amazonaws.com:5432/dfpsub468628mv'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = heruko
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
app.config.from_object(__name__)
from app import views
