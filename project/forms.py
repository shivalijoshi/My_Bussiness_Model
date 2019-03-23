from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class SignUp(FlaskForm):
	username=StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
	email=StringField('Email',validators=[DataRequired(), Email()])
	password=PasswordField('Password', validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField('Sign Up')

class LogIn(FlaskForm):
	email=StringField('Email',validators=[DataRequired(), Email()])
	password=PasswordField('Password', validators=[DataRequired()])
	remember=BooleanField('remember me')
	submit=SubmitField('Log In')


	