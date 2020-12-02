from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PostForm(FlaskForm):

    title = StringField('title',validators=[Required()])
    content = TextAreaField('Post', validators=[Required()])
    
    submit = SubmitField('Submit')

 

class CommentForm(FlaskForm):
    comment = TextAreaField('Your Comment....',validators=[Required()])
  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
 