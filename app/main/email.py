# -*- coding: utf-8 -*-
from flask import current_app, render_template
from flask.ext.mail import Message
from .. import mail
from threading import Thread
import datetime


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(data):
    app = current_app._get_current_object()
    datTime = datetime.datetime.now()
    msg = Message(u'Запрос '+datTime.strftime('%Y/%m/%d %H:%M:%S'), sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_USERNAME']])

    msg.body = render_template('emailQuery.txt', data=data)
    mail.send(msg)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr