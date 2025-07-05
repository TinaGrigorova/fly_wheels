from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('alloy/', views.alloy_wheels, name='alloy_wheels'),  
    path('track/', views.track_edition, name='track_edition'),
]