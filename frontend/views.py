# Create your views here.
from django.http import HttpResponse
from functions import conn_varnish

def index_view(request):

    text = "<pre>" , conn_varnish() , "<pre>"
    return HttpResponse(text)



