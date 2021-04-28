from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required

from datetime import datetime

from app import db
from app import myapp
from app.forms import LoginForm, TaskForm, SignUpForm

from app.models import User, Task

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

    return render_template('login.html', title='Sign In', form=form)

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
            flash('Account Created')
	
    return render_template('create_account.html', title='Create Account', form=form)

@myapp.route('/taskmenu', methods = ['GET', 'POST'])
def taskmenu():
    #@login_required
   form = TaskForm()
   if form.validate_on_submit():
	    # create the new task
        new_task = Task(task_name = form.task_name.data, task_description = form.task_description.data)
        new_task.set_deadline(form.deadline.data)
        db.session.add(new_task)
        db.session.commit()
   
   posts = []
   alltask = Task.query.all()
   if alltask is not None:
       for atask in alltask:
            posts = posts + [
            {	'Name':f'{atask.task_name}', 
                'Description':f'{atask.task_description}',
		        'Deadline':f'{atask.deadline.strftime("%m/%d/%Y")}',
                'id':f'{atask.id}',
                'completed':f'{atask.completed}'
            }
            ] 

   return render_template('taskmenu.html', title='Task', form=form, posts=posts)

@myapp.route('/deletetask/<int:id>')
def deletetask(id):
    task_to_delete = Task.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/taskmenu')

@myapp.route('/checktask/<int:id>')
def checktask(id):
    task_to_check = Task.query.get_or_404(id)
    if task_to_check.completed == False:
        task_to_check.completed = True
    else:
        task_to_check.completed = False
    db.session.add(task_to_check)
    db.session.commit()
    return redirect('/taskmenu')
