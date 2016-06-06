from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash, request, current_app
from . import main
from forms import QueryForm
from flask.ext.mail import Message
from email import send_email


@main.route('/<lang_code>', methods=['GET', 'POST'])
def index(lang_code):

    return render_template('index.html', lang_code=lang_code)


@main.route('/<lang_code>/about', methods=['GET', 'POST'])
def about(lang_code):
    return render_template('about.html', lang_code=lang_code)
    #return render_template('about.html')


@main.route('/<lang_code>/services', methods=['GET', 'POST'])
def services(lang_code):
    return render_template('services.html', lang_code=lang_code)


@main.route('/<lang_code>/querypage', methods=['GET', 'POST'])
def querypage(lang_code):

    if request.method == 'POST':
        print 'adadfasdfasdf'
        send_email(request.form)
        return redirect(url_for('index'))
    return render_template('querypage.html', lang_code=lang_code)


@main.route('/<lang_code>/geography', methods=['GET', 'POST'])
def geography(lang_code):

    return render_template('geography.html', lang_code=lang_code)


@main.route('/<lang_code>/info', methods=['GET', 'POST'])
def info(lang_code):

    return render_template('info.html', lang_code=lang_code)


@main.route('/<lang_code>/contact', methods=['GET', 'POST'])
def contact(lang_code):

    return render_template('contact.html', lang_code=lang_code)


@main.route('/change_lang', methods=['GET', 'POST'])
def change_lang():

    if request.method == 'GET':
        print request.url
        lang = request.args.get('lang')
        print request.args.get('cur')
        try:
            url = request.args.get('cur').split('/')[2]
        except:
            return redirect(lang)
        return redirect(lang+'/'+url)
    return redirect('/info')










