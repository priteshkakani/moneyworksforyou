from django.urls import path

import stocks
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path("", views.index, name='index'),
    path('stocks/', views.stocks, name='stocks'),
    path('stocks/details/<int:id>', views.details, name='details')
]
