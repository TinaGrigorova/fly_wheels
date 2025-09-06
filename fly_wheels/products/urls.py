from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('alloy/', views.alloy_wheels, name='alloy_wheels'),
    path('track/', views.track_edition, name='track_edition'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
    path('my-orders/', views.order_history, name='order_history'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('brand/<str:brand>/', views.filter_by_brand, name='filter_by_brand'),
    path('size/<str:size>/', views.filter_by_size, name='filter_by_size'),
    path('weight/<str:weight>/', views.filter_by_weight, name='filter_by_weight'),
]
