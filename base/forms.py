from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, SelectDateWidget
from django.forms.widgets import DateInput, TimeInput, SplitDateTimeWidget

from .models import UserModel, MenuModel, GamesModel, OrdersModel


class MyUserCreationForm(UserCreationForm):
    '''
    Форма регистрации
    '''
    class Meta:
        model = UserModel
        fields = ['name', 'phone', 'password1', 'password2']


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


class OrdersForm(ModelForm):
    """
    Форма для брони
    """
    class Meta:
        model = OrdersModel
        fields = ['order_date']

        widgets = {
            'order_date': SplitDateTimeWidget(
                date_attrs={'type': 'date'},
                time_attrs={'type': 'time'},
                time_format='%H-%M'
            )
        }