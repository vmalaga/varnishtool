django-varnish-admin
====================

Admin fronted for varnish 3

Install instructions
--------------------
* You need a local Varnish server
* Also you need a minimal build developement tools like gcc

Python libs
===========
Is better to work with virtualenv and use of virtualenvwrapper is easy

```bash
# apt-get install virtualenvwrapper libmysqlclient-dev python-dev
# mkvirtualenv djvaradm
# workon djvaradm
# (djvaradm)# pip install -r requirements.txt
# (djvaradm)# ./manage.py syncdb
```


Issues
======
if you get [Errno 13] Permission denied: '/etc/varnish/secret' must change permissions on varnish secret file

```
# sudo chmod 666 /etc/varnish/secret
```
