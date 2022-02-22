from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage , name='home'),
    path('check_reservations', views.CheckOrdersPage , name='check_reservations'),
    path('make_reservation', views.MakeOrderPage , name='make_order'),
    path('register', views.registerPage , name='register'),
    path('register/process', views.processRegistration , name='register-process'),
    path('logout', views.logoutPage , name='logout'),
    path('login', views.loginPage , name='login'),
    path('logout/process', views.processLogin , name='login-process'),
]