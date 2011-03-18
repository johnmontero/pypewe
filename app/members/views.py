#-*- coding: utf-8 -*-

from app import app
from flask import render_template
from members.models import Member
from members.forms import MemberForm
from utils.decorators import login_required


@app.route('/miembros/')
def member_list():
    """
    Renders the list of current members
    """
    members = Member.all()
    return render_template('members/list.html', members=members)



@app.route('/miembro/edit', methods = ['GET', 'POST'])
@login_required
def member_edit():
    """
    """
    form = MemberForm()
    if form.validate_on_submit():
        member = Member(firstname = form.firstname.data,
                    lastname = form.lastname.data,
                    location = form.location.data,
                    user = users.get_current_user())
        member.put()
        flash('Member saved on database.')
        return redirect(url_for('member_list'))
    return render_template('members/edit.html', form=form)
