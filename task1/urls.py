from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.task1, name='task1'),
    path(r'read-notes', views.read_notes, name='read-notes'),
]
