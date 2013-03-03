from functions import *
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    version = varnishVersion()
    stats = varnish_stats()
    stats.get_stats()
    client_stats = stats.client_st()
    cache_stats = stats.cache_st()
    backend_stats = stats.backend_st()
    return render_to_response('frontend/index.html',
        {'version':version,
        'client_stats':client_stats,
        'cache_stats': cache_stats,
        'backend_stats': backend_stats})

def tablestats_view(request):
    stats = varnish_stats()
    return render_to_response('frontend/table.html', {'varnish_stats':stats})
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
