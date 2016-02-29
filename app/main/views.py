from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash, request
from . import main
from forms import QueryForm
from flask.ext.mail import Message
from app import mail
from email import send_email

@main.route('/about', methods=['GET', 'POST'])
def about():

    return render_template('about.html')


@main.route('/services', methods=['GET', 'POST'])
def services():

    return render_template('services.html')


@main.route('/querypage', methods=['GET', 'POST'])
def querypage():

    if request.method == 'POST':

        send_email()
        print '______________'
        print request.method
        #print request.form['shipper']
        #print request.form.get('age')
    return render_template('querypage.html')


@main.route('/geography', methods=['GET', 'POST'])
def geography():

    return render_template('geography.html')


@main.route('/info', methods=['GET', 'POST'])
def info():

    return render_template('info.html')


@main.route('/contact', methods=['GET', 'POST'])
def contact():

    return render_template('contact.html')







