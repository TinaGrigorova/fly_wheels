from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("newsletter/subscribe/", views.newsletter_subscribe, name="newsletter-subscribe"),
    path("newsletter/unsubscribe/", views.newsletter_unsubscribe, name="newsletter-unsubscribe"),
]
