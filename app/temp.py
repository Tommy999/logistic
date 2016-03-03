from flask import Flask
from flask.ext.mail import Mail
from flask.ext.mail import Message

DEBUG = True
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'moustachedtom@gmail.com'
MAIL_PASSWORD = '23931174Tolian'

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

msg =Message('test subject', sender='moustachedtom@gmail.com', recipients=['moustachedtom@gmail.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'

mail.send(msg)