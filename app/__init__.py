from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    db.init_app(app)

    from app.home import home as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/')

    from app.supdomain import supdomain as supdomain_blueprint
    app.register_blueprint(supdomain_blueprint, url_prefix='/supdomain')

    from app.domain import domain as domain_blueprint
    app.register_blueprint(domain_blueprint, url_prefix='/domain')

    from app.formula import formula as formula_blueprint
    app.register_blueprint(formula_blueprint, url_prefix='/formula')

    from app.picture import picture as picture_blueprint
    app.register_blueprint(picture_blueprint, url_prefix='/picture')

    return app