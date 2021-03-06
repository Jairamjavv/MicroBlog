import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # CSRF token key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-other-key'

    # sql database URL
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///'+os.path.join(basedir, 'app.db')
    
    # signal the application every time a change is about to be made in the database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
