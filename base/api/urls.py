from django.urls import path

from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('freetables/', views.getFreeTables),
    path('menu/', views.getMenuPositions),
    path('games/', views.getGames),
]