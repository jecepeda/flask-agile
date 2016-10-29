from app import create_app
from app.models import db, User
from flask_script import Manager, Shell
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)

@manager.command
def dropdb():
    db.drop_all()

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def createdb():
    db.create_all()

if __name__ == "__main__":
    manager.run()
