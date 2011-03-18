#-*- coding: utf-8 -*-


from flaskext import wtf
from flaskext.wtf import validators

class MemberForm(wtf.Form):
    firstname = wtf.TextField('Firstname', validators=[validators.Required()])
    lastname = wtf.TextField('Lastname', validators=[validators.Required()])
    location =  wtf.TextField('Location', validators=[validators.Required()])
