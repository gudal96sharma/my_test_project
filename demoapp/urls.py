from django.contrib import admin
from django.urls import path, include
# from .master import views
from demoapp import views

from django.conf.urls import url
from .views import *

app_name = 'demoapp'


urlpatterns = [

	path('', views.index, name='index'),
	path('post_id/<id>/', views.post_id, name='post_id'),
	path('show_more/', views.show_more, name = "show_more"),

]
