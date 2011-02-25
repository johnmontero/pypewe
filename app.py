#-*- coding: utf-8 -*-

from google.appengine.ext.webapp.util import run_wsgi_app
from flask import Flask

import settings

app = Flask('pypewe')
app.config.from_object('settings')

from website import views as website_views

run_wsgi_app(app)
