from functions import *
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse



@login_required
def index_view(request):
    version = varnishVersion()
    stats = varnish_stats()
    stats.get_stats()
    client_stats = stats.client_st()
    cache_stats = stats.cache_st()
    backend_stats = stats.backend_st()
    memory_stats = stats.memory_st()
    return render_to_response('frontend/index.html',
        {'version':version,
        'client_stats':client_stats,
        'cache_stats': cache_stats,
        'backend_stats': backend_stats,
        'memory_stats': memory_stats,
        'page': 'index'})
    
import simplejson as json
def api_view(request,statname):
    stats = varnish_stats()
    stats.get_stats()
    if statname == "client_stats":
        result = stats.client_st()
    elif statname == "cache_stats":
        result = stats.cache_st()
    elif statname == "backend_stats":
        result = stats.backend_st()
    elif statname == "memory_stats":
        result = stats.memory_st()
    else:
        result = ""
    return HttpResponse(json.dumps(result), mimetype="application/json")

def vcledit_view(request):
    version = varnishVersion()
    vcltext = getVcl()
    return render_to_response('frontend/vcledit.html',
        {'vcltext':vcltext,
        'page': 'vcledit',
        'version':version})
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def test_view(request):
    return render_to_response('frontend/test.html',
        {'page': 'index'}
        )