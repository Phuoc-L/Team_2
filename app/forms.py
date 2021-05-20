from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    username = StringField('Create Username', validators = [DataRequired()])
    password = PasswordField('Create Password', validators = [DataRequired()])
    submit = SubmitField('Create Account')

class TaskForm(FlaskForm):
    task_name = StringField('Name of Task', validators = [DataRequired()])
    task_description = StringField('Task Description', validators = [DataRequired()])
    deadline = StringField('Deadline (mm/dd/yyyy)', validators = [DataRequired()])
    submit = SubmitField('Create Task')

class EditForm(FlaskForm):
    task_name = StringField('New Task Name')
    task_description = StringField('New Description')
    deadline = StringField('New Deadline (mm/dd/yyy)')
    submit = SubmitField('Submit Changes')

class CheckOffTaskForm(FlaskForm):
    date_completed = StringField('Date Completed (mm/dd/yyyy)', validators = [DataRequired()])
    submit = SubmitField('Submit Changes')
    
class TeamForm(FlaskForm):
    team_name = StringField("Name of Team", validators = [DataRequired()])
    add_user = StringField("Name of User", validators = [DataRequired()])
    submit = SubmitField('Create Team')

class AssignTeamForm(FlaskForm):
    team = StringField('Name of Team', validators = [DataRequired()])
    submit = SubmitField('Submit Changes')




