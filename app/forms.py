from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

# Forms short link

class ShortLinkForm(FlaskForm):
    long_url = StringField('Enter a URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Shorten')