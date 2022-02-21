from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import UserModel, MenuModel, GamesModel


class MyUserCreationForm(UserCreationForm):
    '''
    Форма регистрации
    '''
    class Meta:
        model = UserModel
        fields = ['name', 'phone', 'password_1', 'password_2']


class MenuForm(ModelForm):
    """
    Форма меню
    """
    class Meta:
        model = MenuModel
        fields = '__all__'


class GamesForm(ModelForm):
    """
    Форма для игр
    """
    class Meta:
        model = GamesModel
        fields = '__all__'
