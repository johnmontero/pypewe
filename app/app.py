#-*- coding: utf-8 -*-
import os
import sys

if 'lib' not in sys.path:
    # Add lib as primary libraries directory, with fallback to lib/dist
    # and optionally to lib/dist.zip, loaded using zipimport.
    sys.path[0:0] = ['lib', 'lib/dist', 'lib/dist.zip']


from google.appengine.ext.webapp.util import run_wsgi_app
from flask import Flask

import settings

app = Flask('pypewe')
app.config.from_object('settings')

from website import views as website_views

run_wsgi_app(app)
