from functions import *
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    version = varnishVersion()
    stats = varnish_stats()
    varnish = conn_varnish()
    if type(varnish) == str:
        banner = varnish
        stats = ""
    else:
        banner = varnish.command('banner').splitlines()
    return render_to_response('frontend/index.html',{'banner':banner,
                                                     'version':version,
                                                     'varnish_stats':stats})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def status_view(request):
    pass


