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

    from .api_1_0_0 import api as api_1_0_0_blueprint

    app.register_blueprint(api_1_0_0_blueprint, url_prefix='/api/v1.0.0')

    from .api_1_0_0 import encoder
    app.json_encoder = encoder.IMicrobeEncoder

    return app
