# -*- coding: utf-8 -*-
from django.conf.urls import url
from ProTwo import views



urlpatterns = [
    url(r'^$',views.users,name='users')
]