from pprint import pprint

from flask import Flask
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy

from config import configs


db = SQLAlchemy()


from app import models
from app.model_view import iMicrobeModelView, ProjectView, SampleView


def create_app(config_name):
    app_ = Flask(__name__)

    app_.config.from_object(configs[config_name])

    configs[config_name].init_app(app_)

    basic_auth = BasicAuth(app_)
    db.init_app(app_)

    #from .main import main as main_blueprint
    #app_.register_blueprint(main_blueprint)

    #from .imicrobe import imicrobe as imicrobe_api_blueprint
    #app_.register_blueprint(imicrobe_api_blueprint, url_prefix='/flask')

    from .imicrobe import encoder
    app_.json_encoder = encoder.IMicrobeEncoder

    admin = Admin(
        app_,
        name='iMicrobe Administration Console',
        template_mode='bootstrap3',
        url=app_.ADMIN_URL)

    for model_class in models.__dict__.values():
        if isinstance(model_class, type) and model_class.__module__ == models.__name__:
            print('found model class "{}"'.format(model_class.__name__))
            if model_class.__name__ == 'Project':
                view = ProjectView(model_class, db.session)
            elif model_class.__name__ == 'Sample':
                view = SampleView(model_class, db.session)
            else:
                view = iMicrobeModelView(model_class, db.session)
            admin.add_view(view)
        else:
            pass
            # print('"{}" is not a database model'.format(models_class))

    return app_

"""
    # so far haven't gotten this to work....
    #
    # construct the name of a specific View using the model_class.__name__
    # for example if model_class.__name__ is 'Sample' look for a view called 'SampleView'
    # if 'SampleView' exists in the model_view module then instantiate it
    # otherwise use the generic iMicrobeModelView
    for model_class in models.__dict__.values():
        if isinstance(model_class, type) and model_class.__module__ == models.__name__:
            print('found model class "{}"'.format(model_class.__name__))
            specific_model_view_class_name = model_class.__name__ + 'View'
            if hasattr(model_view, specific_model_view_class_name):
                print('nailed it: {}'.format(specific_model_view_class_name))
                view_class = getattr(model_view, specific_model_view_class_name)
                print('found view class "{}"'.format(view_class))
                view = view_class(model_class, db.session)
            else:
                #view = model_view.iMicrobeModelView(model_class, db.session)
                view_class = getattr(model_view, 'iMicrobeModelView')
                print('using class {}'.format(view_class))
                view = view_class(model_class, db.session)
            admin.add_view(view)
        else:
            pass
            #print('"{}" is not a database model'.format(models_class))
"""
