# same as
# from app import db
from app import db
from datetime import datetime
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = False)
    # email = db.Column(db.String(32), unique = True, nullable = False, index = True)
    password = db.Column(db.String(200), unique = False)
    #tasks = db.relationship('Task', backref = 'author', lazy = 'dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)    
        
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task_name = db.Column(db.String(256))
    task_description = db.Column(db.String(256))
    deadline = db.Column(db.DateTime, index = True, unique = False)
    completed = db.Column(db.Boolean, default = False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def set_deadline(self, deadline):
        self.deadline = datetime.strptime(deadline, '%m/%d/%Y')
    
    def __repr__(self):
        return '<Task {}>'.format(self.task_description)

@login.user_loader
def load_user(id):
    return User.query.get(int(id)) 