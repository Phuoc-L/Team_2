from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required


from datetime import datetime

from app import db
from app import myapp
from app.forms import LoginForm, TaskForm, SignUpForm, EditForm, TeamForm, AssignTeamForm, CheckOffTaskForm

from app.models import User, Task, Team

# different URL the app will implement
@myapp.route("/")
# called view functiondef
def begin():
	return redirect('/login')

@myapp.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # User.query.filter_by() returns a list from the User table
        # first() returns first element of the list
        # the form.username.data is getting the info the user submitted in the form
        user = User.query.filter_by(username = form.username.data).first()
        # if no user found or password for user incorrect
        # user.check_password() is a method in the User class
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        # let flask_login library know what user logged int
        # it also means that their password was correct
        login_user(user, remember = form.remember_me.data)
        # return to page before user got asked to login
        # for example, if user tried to access a wedpage called profile, but since they
        # weren't logged in they would get redirected to login page. After they log in
        # the user will be redirected to their previous request, which would be the profile
        # page in this case.
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('taskmenu')

        return redirect(next_page)

    return render_template('login.html', title = 'Sign In', form = form)

@myapp.route("/req")
# user needs to be logged in to see this page
# needs to be user route!
@login_required
# called view function
def req():
    return '''<html><body>
    User needs to be logged in
    </body>
    </html>'''

@myapp.route('/Logout')
def Logout():
	logout_user()
	flash('You are logged out')
	return redirect('/login')

@myapp.route('/CreateAccount', methods = ['GET', 'POST'])
def Create_Account():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        # if not create user and add to database
        if user is None:
            new_user = User(username = form.username.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash(f'The user {form.username.data} is created')
            return redirect('/login')
        elif user is not None:
            flash(f'The user {form.username.data} already exist.')
        
	
    return render_template('create_account.html', title = 'Create Account', form = form)

@myapp.route('/taskmenu', methods = ['GET', 'POST'])
def taskmenu():
    #@login_required
    

    posts = []
    alltask = Task.query.all()
    if alltask is not None:
        for atask in alltask:
            if atask.date_completed is not None and atask.team is None:
                posts = posts + [
                {	'Name':f'{atask.task_name}', 
                    'Description':f'{atask.task_description}',
                    'Deadline':f'{atask.deadline.strftime("%m/%d/%Y")}',
                    'id':f'{atask.id}',
                    'completed':f'{atask.completed}',
                    'datecompleted':f'{atask.date_completed.strftime("%m/%d/%Y")}',
					'team':'None'
                }
                ] 
            elif atask.date_completed is not None and atask.team is not None:
                posts = posts + [
                {	'Name':f'{atask.task_name}', 
                    'Description':f'{atask.task_description}',
                    'Deadline':f'{atask.deadline.strftime("%m/%d/%Y")}',
                    'id':f'{atask.id}',
                    'completed':f'{atask.completed}',
                    'datecompleted':f'{atask.date_completed.strftime("%m/%d/%Y")}',
					'team':f'{Team.query.filter_by(id = atask.team).first().team}'
                }
                ]
            elif atask.date_completed is None and atask.team is not None:
                posts = posts + [
                {	'Name':f'{atask.task_name}', 
                    'Description':f'{atask.task_description}',
                    'Deadline':f'{atask.deadline.strftime("%m/%d/%Y")}',
                    'id':f'{atask.id}',
                    'completed':f'{atask.completed}',
					'team':f'{Team.query.filter_by(id = atask.team).first().team}'
                }
                ]  
            else:
                posts = posts + [
                {	'Name':f'{atask.task_name}', 
                    'Description':f'{atask.task_description}',
                    'Deadline':f'{atask.deadline.strftime("%m/%d/%Y")}',
                    'id':f'{atask.id}',
                    'completed':f'{atask.completed}',
					'team':'None'
                }
                ]

    return render_template('taskmenu.html', title = 'Task', posts = posts)

@myapp.route('/createtask', methods = ["GET","POST"])
def CreateTask():
    form = TaskForm()
    if form.validate_on_submit():
        # create the new task
        new_task = Task(task_name = form.task_name.data, task_description = form.task_description.data)
        new_task.set_deadline(form.deadline.data)
        db.session.add(new_task)
        db.session.commit()
        flash('New Task Created')
        return redirect('/taskmenu')
    return render_template('createtask.html', title='Create Task', form=form)


@myapp.route('/deletetask/<int:id>')
def DeleteTask(id):
    task_to_delete = Task.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    flash('Task Has Been Deleted')
    return redirect('/taskmenu')

@myapp.route('/checktask/<int:id>', methods = ["GET","POST"])
def CheckTask(id):
    form = CheckOffTaskForm()
    if form.validate_on_submit():
        task_to_check = Task.query.get_or_404(id)
        task_to_check.set_date_completed(form.date_completed.data)
        task_to_check.completed = True
        db.session.add(task_to_check)
        db.session.commit()
        return redirect("/taskmenu")  
    posts = []
    posts = posts + [{}]    
    return render_template('checkoff.html', title='Check off task', form=form, posts=posts)

@myapp.route('/unchecktask/<int:id>')
def UncheckTask(id):
    task_to_uncheck = Task.query.get_or_404(id)
    task_to_uncheck.date_completed = None
    task_to_uncheck.completed = False
    db.session.add(task_to_uncheck)
    db.session.commit()
    return redirect("/taskmenu") 


@myapp.route("/edit/<int:id>", methods = ["GET","POST"])
def EditTask(id):
    form = EditForm()
    if form.validate_on_submit():
        task = Task.query.get_or_404(id)
        if form.task_name.data is not '':
            task.task_name = form.task_name.data
        if form.task_description.data is not '':
            task.task_description = form.task_description.data
        if form.deadline.data is not '':
            task.set_deadline(form.deadline.data)
        db.session.add(task)
        db.session.commit()
        flash("Task Has Been Edited")
        return redirect("/taskmenu")

    return render_template('editForm.html', title='Edit Task', form=form)


@myapp.route("/taskinfo/<int:id>")
def taskInfo(id):
    task_to_view = Task.query.get_or_404(id)
    if task_to_view.date_completed is None:
        date_completed = 'None'
    else:
        date_completed = task_to_view.date_completed.strftime("%m/%d/%Y")
    if task_to_view.team is not None:
        team = team = Team.query.filter_by(id = task_to_view.team).first().team
    else:
        team = 'None'
    return render_template('taskinfo.html', title='TaskInfo', name = task_to_view.task_name, description = task_to_view.task_description, deadline = task_to_view.deadline.strftime("%m/%d/%Y"), date_completed = date_completed, team = team)

@myapp.route("/AssignTask/<int:id>", methods = ["GET","POST"])
def AssignTeam(id):
    form = AssignTeamForm()
    if form.validate_on_submit():
        team = Team.query.filter_by(team = form.team.data).first()
        if team is None:
            flash(f'The team {form.team.data} does not exist')
            return redirect(f"/AssignTask/{id}")
        task = Task.query.get_or_404(id)
        task.team = team.id
        db.session.add(task)
        db.session.add(team)
        db.session.commit()
        return redirect("/taskmenu")
    
    posts = []
    posts = posts + [{}]    

    return render_template('assigntask.html', title = 'Assign Task', form = form, posts = posts)

@myapp.route("/team", methods = ["GET","POST"])
def createTeam():
    form = TeamForm()
    if form.validate_on_submit():
        team = Team.query.filter_by(team = form.team_name.data).first()
        if team is None:
            new_team = Team(team = form.team_name.data)
            db.session.add(new_team)
            flash(f'Team {form.team_name.data} is created')
        
        tuser = User.query.filter_by(username = form.add_user.data).first()

        if tuser is None:
            flash(f'The user {form.add_user.data} does not exist')
            return redirect("/team")
        tuser.team = Team.query.filter_by(team = form.team_name.data).first().id
        db.session.add(tuser)
        db.session.commit()
        flash(f'The user {form.add_user.data} was added to team {form.team_name.data}')
        #return redirect("/taskmenu")
        
    posts = []
    posts = posts + [{}]

    return render_template('team.html', title = 'Team Name', form = form, posts = posts)
