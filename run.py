from app import myapp, db

db.create_all()

myapp.run()