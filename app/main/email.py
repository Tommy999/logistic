from flask.ext.mail import Message
import app
from app import mail
import config

def send_email():
    print '_________________________________________________'
    print config
    print app.config
    msg = Message('safasdfasdftest',
    sender=app.config['MAIL_USERNAME'], recipients=app.config['MAIL_USERNAME'])
    msg.body = 'qwrewe'
    msg.html = '<b>asdfasdf</b>'
    mail.send(msg)