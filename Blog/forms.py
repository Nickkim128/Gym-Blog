#this uses the Flask extension to use python class which automatically converts to html
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrateForm(FlaskForm):
	#each of these are form fields for specific parts of a website
	#validators add specific requirements for each field
	username = StringField("Username", 
							validators = [DataRequired(), Length(min = 5, max = 15)])
	email = StringField("Email", validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired(), Length(min = 2, max = 10)])
	confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo("password")])
	submit = SubmitField("Register")

class LoginForm(FlaskForm):
	#each of these are form fields for specific parts of a website
	email = StringField("Email", validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	submit = SubmitField("Login")
	remember = BooleanField("Remember Account")
