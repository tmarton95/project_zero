from django.urls import path
from .views import home, contact, about, services

urlpatterns = [
    path('', home, name="home"),
    path('services/', services, name="services"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
]