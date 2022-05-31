from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.indexPage, name = 'indexPage'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
]