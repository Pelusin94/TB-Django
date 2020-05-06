from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.main_response,name='main_page'),
    path('fulfilment/', views.fulfilment_response,name='fulfilment_page'),
]
