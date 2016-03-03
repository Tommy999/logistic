import os
basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig():
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'moustachedtom@gmail.com'
    MAIL_PASSWORD = '23931174Tolian'
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    @staticmethod
    def init_app(app):
        pass



