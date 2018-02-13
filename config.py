import os

from flask_debugtoolbar import DebugToolbarExtension

#basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 60  # should be less than DB connection timeout
    SQLALCHEMY_DATABASE_URI = os.environ.get('IMICROBE_DB_URI')

    SECRET_KEY = os.environ.get('IMICROBE_FLASK_SESSION_SECRET_KEY')

    BASIC_AUTH_USERNAME = os.environ.get('IMICROBE_FLASK_ADMIN_UN')
    BASIC_AUTH_PASSWORD = os.environ.get('IMICROBE_FLASK_ADMIN_PW')
    BASIC_AUTH_FORCE = True

    def init_app(self, app):
        app.ADMIN_URL = self.ADMIN_URL


class DevelopmentConfig(Config):
    DEBUG = True
    # this url can coexist with /imicrobe/admin on a development server
    ADMIN_URL = '/imicrobe/admin'

    def init_app(self, app):
        Config.init_app(self, app)
        toolbar = DebugToolbarExtension(app)


class ProductionConfig(Config):
    DEBUG = True
    ADMIN_URL = '/admin'

    def init_app(self, app):
        Config.init_app(self, app)
        toolbar = DebugToolbarExtension(app)


configs = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig()
}
