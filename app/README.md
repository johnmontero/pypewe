PyPeWe
======

PyPeWe is a GAE-powered custom CMS for Python User Groups which is still in its very early stages.

It is being written to be running behind http://python.pe which is currently a work in progress.

Developers:

In order to run PyPeWe locally for development purposes just do the following:

a) Grab a copy of the Google AppEngine SDK for Python and install it.

wget -c http://googleappengine.googlecode.com/files/google_appengine_1.4.2.zip

unzip google_appengine_1.4.2.zip

mkdir /opt/google

mv google_appengine /opt/google/appengine

b) Run the project

/opt/google/appengine/dev_appserver.py pypewe/

Point your browser to http://localhost:8080/

(C) 2011 - Python Peru - http://python.pe
