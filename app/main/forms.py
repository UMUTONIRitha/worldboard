from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PostForm(FlaskForm):

 title = StringField('title',validators=[Required()])
 content = TextAreaField('Post', validators=[Required()])
 country_name = TextAreaField('Country', validators=[Required()])
 submit = SubmitField('Submit')
 