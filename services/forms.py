from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,EqualTo,BooleanField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    subject = StringField('Subject',validators=[DataRequired()])
    message = TextAreaField('Message',validators=[DataRequired])
    
    submit = SubmitField('Send')
    

# class RegistrationForm(FlaskForm):

class LoginForm(FlaskForm):
    # username = StringField('username',validators=[DataRequired(), Length(min=3, max=20)])
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ProjectForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired])
    # slug = StringField('Slug',validators=[DataRequired])
    description = StringField('Description',validators=[DataRequired])
    summary = TextAreaField('Summary',validators=[DataRequired])