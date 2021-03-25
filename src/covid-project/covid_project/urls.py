# -*- coding: utf-8 -*-
"""
@author: Venkata Sai Madhav Kaza
"""

from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.views.generic import TemplateView

urlpatterns =[
    url(r'^$', views.index, name='home'),
    url(r'^output$', views.output,name='output'),
    url(r'^report$', views.report,name='report'),
    url(r'^prediction$',views.prediction,name="prediction")
]
urlpatterns += staticfiles_urlpatterns()