from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class TaskForm(FlaskForm):
    task_name = StringField('Name of Task', validators = [DataRequired()])
	#task_description = StringField('Task Description', validators = [DataRequired()])
	#deadline = 
	#group =
	#team = 

class LogoutForm(FlaskForm):
    Logout  = SubmitField('Logout')


