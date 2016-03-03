from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from config_short import DevelopmentConfig


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(DevelopmentConfig)
    DevelopmentConfig.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


