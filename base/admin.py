from django.contrib import admin
from .models import UserModel, MenuModel, GamesModel, OrdersModel


admin.site.register(UserModel)
admin.site.register(MenuModel)
admin.site.register(GamesModel)
admin.site.register(OrdersModel)
