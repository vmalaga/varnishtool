from django.conf.urls import *
from frontend.views import *

urlpatterns = patterns('',

                       # Main web portal entrance.
                       (r'^$', portal_main_page),

                       )
