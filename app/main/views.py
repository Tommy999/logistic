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

