from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('learn/', views.learning),
    path('check/', views.checking),
    path('table/', views.db_table),
]
