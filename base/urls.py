from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage , name='home'),
    path('check_reservations', views.CheckOrdersPage , name='check_reservations'),
    path('make_reservation', views.MakeOrderPage , name='make_order')
]