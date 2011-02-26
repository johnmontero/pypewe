#-*- coding: utf-8 -*-

from google.appengine.ext import db

from members import strings, constants
from countries import constants as countries_constants

class Member(db.Model):
    user = db.UserProperty(required=True)
    firstname = db.StringProperty(required=True)
    lastname = db.StringProperty(required=True)
    gender = db.StringProperty(required=True,
        choices=constants.GENDER_CHOICES)
    country_of_birth = db.StringProperty(required=True,
        choices=countries_constants.COUNTRY_CHOICES)
    country_of_residence = db.StringProperty(required=True,
        choices=countries_constants.COUNTRY_CHOICES)
    birthdate = db.DateProperty(required=True)
    occupation = db.StringProperty(required=True, 
        choices=constants.OCCUPATION_CHOICES)
    website = db.LinkProperty()
    blog = db.LinkProperty()
    company_name = db.StringProperty()
    company_website = db.LinkProperty()
    twitter = db.StringProperty()
    facebook = db.LinkProperty()
    location = db.StringProperty()

    def __unicode__(self):
        return u'%s' % self.get_full_name()

    def get_full_name(self):
        return '%s %s' % (self.firstname, self.lastname)

    def get_formal_name(self):
        return '%s, %s' % (self.lastname, self.firstname)

    def get_gender_display(self):
        return constants.GENDER_DICT[self.gender] 

    def get_occupation_display(self):
        return constants.OCCUPATION_DICT[self.occupation] 

    def get_country_of_birth_display(self):
        return constants.COUNTRY_DICT[self.country_of_birth] 

    def get_country_of_residence_display(self):
        return constants.COUNTRY_DICT[self.country_of_residence] 
