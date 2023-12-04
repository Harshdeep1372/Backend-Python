# What is Django URLs?make program to create django urls?

'''
This file is responsible for mapping URLs to views in your Django web application.
The urls.py file is part of each Django app and is used to define the URL patterns for that app.
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
