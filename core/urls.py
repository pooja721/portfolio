from django.urls import path
from . import views
from .views import contact, successView
from django.contrib import admin
from django.urls import path

urlpatterns=[
    path('contact.html',views.contact,name='contact'),
    path('contact/', contact, name='contact'),
    path('success/', successView, name='success'),

    ]






