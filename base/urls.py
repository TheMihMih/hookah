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
    path('login/process', views.processLogin , name='login-process'),
    path('delete_reservation/<str:id>', views.deletePage , name='delete_reservation'),
    path('games', views.gamesPage , name='games'),
    path('games/<str:id>', views.singleGamePage , name='singlegame'),
    path('add_game', views.addingGamePage , name='add_game'),
    path('add_game/process', views.addingGameProcess, name='add_game-process'),
    path('delete_game/<str:id>', views.deleteGame , name='delete_game'),

]