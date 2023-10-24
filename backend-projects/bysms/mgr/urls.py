from django.urls import path

from mgr import log

urlpatterns = [

    path('citylog', log.dispatcher),
]