django-varnish-admin
====================

Admin fronted for varnish 3

Install instructions
====================
You need a local Varnish server

Python libs
===========
Is better to work with virtualenv and use of virtualenvwrapper is easy

# apt-get install virtualenvwrapper
# mkvirtualenv djvaradm
# workon djvaradm
(djvaradm)# pip install -r requirements.txt


Issues
======
if you get [Errno 13] Permission denied: '/etc/varnish/secret' must change permissions on varnish secret file
# sudo chmod 666 /etc/varnish/secret

