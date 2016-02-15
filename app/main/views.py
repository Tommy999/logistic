from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from . import main
from app import db




@main.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@main.route('/index_raw', methods=['GET', 'POST'])
def index_raw():

    return render_template('index_raw.html')

@main.route('/index_raw_2', methods=['GET', 'POST'])
def index_raw_2():

    return render_template('index_raw_2.html')

@main.route('/index_raw_3', methods=['GET', 'POST'])
def index_raw_3():

    return render_template('index_raw_3.html')

@main.route('/index_raw_4', methods=['GET', 'POST'])
def index_raw_4():

    return render_template('index_raw_4.html')

@main.route('/index_raw_5', methods=['GET', 'POST'])
def index_raw_5():

    return render_template('index_raw_5.html')

