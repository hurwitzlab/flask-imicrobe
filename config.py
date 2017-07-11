import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('IMICROBE_DB_URI')

    def init_app(self, app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True



class ProductionConfig(Config):
    DEBUG = False


configs = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig()
}
