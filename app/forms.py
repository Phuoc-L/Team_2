from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Create Account')

class TaskForm(FlaskForm):
    task_name = StringField('Name of Task', validators = [DataRequired()])
    task_description = StringField('Task Description', validators = [DataRequired()])
    deadline = StringField('Deadline (mm/dd/yyyy)', validators = [DataRequired()])
	#group = 
	#team = 
    submit = SubmitField('Create Task')





