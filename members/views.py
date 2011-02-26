#-*- coding: utf-8 -*-

from app import app
from flask import render_template
from members.models import Member

@app.route('/miembros/')
def member_list():
    """
    Renders the list of current members
    """
    members = Member.all()
    return render_template('members/list.html')
