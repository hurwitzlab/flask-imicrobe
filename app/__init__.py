from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import configs


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(configs[config_name])

    configs[config_name].init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .imicrobe import imicrobe as imicrobe_api_blueprint
    app.register_blueprint(imicrobe_api_blueprint, url_prefix='/imicrobe')

    from .imicrobe import encoder
    app.json_encoder = encoder.IMicrobeEncoder

    return app
