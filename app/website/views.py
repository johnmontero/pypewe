#-*- coding: utf-8 -*-

from app import app
from flask import render_template
from members import views as members_views

@app.route('/')
def index():
    """
    Renders the index for the current site
    """
    return render_template('index.html')
