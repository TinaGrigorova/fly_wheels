from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('alloy/', views.alloy_wheels, name='alloy_wheels'),  
    path('track/', views.track_edition, name='track_edition'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
]
