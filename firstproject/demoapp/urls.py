
from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
    path('wish/', views.wish),

]
