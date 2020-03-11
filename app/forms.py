from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import Email

class UploadForm(FlaskForm):
    image = FileField('Image', validators = [FileRequired(), FileAllowed(['jpg','png','Images only!'])])
    
