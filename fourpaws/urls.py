from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.main_view,name='main_page'),
    path('fulfilment/', views.fulfilment_view,name='fulfilment_page'),
]
