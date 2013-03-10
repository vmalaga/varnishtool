VarnishTool
====================

This is a tool to admin varnish 3, with dashboard, statistics, vcl editor, ban urls, etc

Install instructions
--------------------
* You need a local Varnish server
* Also you need a minimal build developement tools like gcc

Python venv
-----------
Is better to work with virtualenv and use the use of virtualenvwrapper is easy

```bash
# apt-get install virtualenvwrapper libmysqlclient-dev python-dev
# mkvirtualenv djvaradm
# workon djvaradm
# (djvaradm)# pip install -r requirements.txt
# (djvaradm)# ./manage.py syncdb
```

Run APP
-------
if you want to run the app in real webserver, use the gunicorn with -D to run as daemon
```
# ./manage.py run_gunicorn --bind=0.0.0.0:8000 --error-logfile=/var/log/gunicorn.log -D
```


Issues
======
if you get [Errno 13] Permission denied: '/etc/varnish/secret' is because you are running django with a user that have not permission to read the file and must change permissions on varnish secret file

```
# sudo chmod 666 /etc/varnish/secret
```
