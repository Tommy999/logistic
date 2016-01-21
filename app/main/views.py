from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from . import main
from app import db




@main.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

