from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
from django.core.validators import MaxValueValidator, MinValueValidator


CHOISES = (
        ("Настольная", "Настольная"),
        ("PS", "PS")
    )


class UserModel(AbstractUser):
    """
    Модель регистрации

    """

    name = models.CharField(verbose_name='Имя', max_length=200, null=True)
    email = models.EmailField(
        null=True, blank=True
    )  # Необходим для переопределения родительского поля email
    phone = PhoneNumberField(verbose_name='Телефон', unique=True, null=True)
    username = None

    USERNAME_FIELD = "phone"
    PHONENUMBER_DEFAULT_REGION = "RU"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"Имя пользователя: {self.name}. Телефон: {self.phone}"

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class MenuModel(models.Model):
    """
    Меню бара

    """

    product_name = models.CharField(verbose_name='Наименование продукта', max_length=200, null=True)
    price = MoneyField(max_digits=14, default_currency="RUB")
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Наименование продукта'
        verbose_name_plural = 'Наименования продуктов'



class GamesModel(models.Model):
    """
    Модель для игр
    game_type определяет настольная игра или для playstation

    """
    
    game_name = models.CharField(verbose_name='Название игры', max_length=200, null=True)
    game_type = models.CharField(max_length=50, null=True, choices=CHOISES)
    bio = models.TextField(null=True, blank=True)

    image = models.ImageField(null=True, blank=True, default="avatar.svg")

    def __str__(self):
        return self.game_name

    class Meta:
        verbose_name = 'Название игры'
        verbose_name_plural = 'Названия игр'



class OrdersModel(models.Model):
    """
    Модель для брони столов
    """

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    table = models.IntegerField(
        validators=[MaxValueValidator(15), MinValueValidator(1)]
    )
    order_date = models.DateTimeField(null=True)
    expired_time = models.DateTimeField(null=True)

    def __str__(self):
        return (
            f"Guest: {self.user}, table: №{self.table}, time exp.: {self.expired_time}"
        )
