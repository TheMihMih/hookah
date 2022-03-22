from django.test import TestCase

from base.models import UserModel, OrdersModel, GamesModel, MenuModel


def run_field_parameter_test(
    model, self_, field_and_parameter_value: dict, parameter_name: str
) -> None:
    """Тестирует значение параметра для всех объектов модели"""

    for instance in model.objects.all():
        for field, expected_value in field_and_parameter_value.items():
            parameter_real_value = getattr(
                instance._meta.get_field(field), parameter_name
            )

            self_.assertEqual(parameter_real_value, expected_value)


class TestVerboseNameMixin:
    """Миксин для проверки verbose_name"""

    def run_verbose_name_test(self, model):
        """Метод, тестирующий verbose_name"""

        run_field_parameter_test(
            model, self, self.field_and_verbose_name, "verbose_name"
        )


class TestMaxLengthMixin:
    """Миксин для проверки max_length"""

    def run_max_length_test(self, model):
        """Метод, тестирующий max_length"""

        run_field_parameter_test(model, self, self.field_and_max_length, "max_length")


class MenuTest(TestCase, TestMaxLengthMixin, TestVerboseNameMixin):
    """
    Тесты модели MenuModel
    """

    @classmethod
    def setUpTestData(cls):
        """Заносит данные в БД перед запуском тестов класса"""

        cls.menu = MenuModel.objects.create(
            product_name="test_product", price="200", bio=""
        )
        cls.field_and_max_length = {
            "product_name": 200,
        }
        cls.field_and_verbose_name = {
            "product_name": "Наименование продукта",
        }
        cls.product_name = cls.menu._meta.get_field("product_name")
        cls.price = cls.menu._meta.get_field("price")
        cls.bio = cls.menu._meta.get_field("bio")

    def test_product_name_max_length(self):
        """Тест параметра max_length"""

        super().run_max_length_test(MenuModel)

    def test_verbose_name(self):
        """Тест параметра verbose_name"""

        super().run_verbose_name_test(MenuModel)

    def test_default_currency(self):
        """Тест параметра default_currency"""

        real_default_currency = getattr(self.price, "default_currency")
        self.assertEqual(real_default_currency, "RUB")

    def test_price_max_digits(self):
        """Тест параметра max_digits"""

        real_max_digits = getattr(self.price, "max_digits")
        self.assertEqual(real_max_digits, 14)

    def test_str_method(self):
        """Тест строкового отображения"""

        self.assertEqual(str(self.menu), str(self.menu.product_name))


class GameTest(TestCase, TestMaxLengthMixin, TestVerboseNameMixin):
    """
    Тесты модели GameModel
    """

    @classmethod
    def setUpTestData(cls):
        """Заносит данные в БД перед запуском тестов класса"""

        cls.games = GamesModel.objects.create(
            game_name="test_game",
            game_type="PS",
        )
        cls.field_and_verbose_name = {
            "game_name": "Название игры",
        }
        cls.field_and_max_length = {"game_name": 200, "game_type": 50}
        cls.game_name = cls.games._meta.get_field("game_name")
        cls.game_type = cls.games._meta.get_field("game_type")

    def test_game_name_max_length(self):
        """Тест параметра max_length"""

        super().run_max_length_test(GamesModel)

    def test_game_name_vebose_name(self):
        """Тест параметра verbose_name"""

        super().run_verbose_name_test(GamesModel)

    def test_str_method(self):
        """Тест строкового отображения"""

        self.assertEqual(str(self.games), str(self.games.game_name))


class OrdersTest(TestCase, TestMaxLengthMixin):
    @classmethod
    def setUpTestData(cls):
        """Заносит данные в БД перед запуском тестов класса"""

        cls.users = UserModel.objects.create(name="test_name", phone="+79098654412")

        cls.orders = OrdersModel.objects.create(
            user=UserModel.objects.get(name="test_name"),
            table="3",
            expired_time="2022-02-28 20:00:00",
        )
        cls.user = cls.orders._meta.get_field("user")
        cls.table = cls.orders._meta.get_field("table")
        cls.expired_time = cls.orders._meta.get_field("expired_time")

    def test_str_method(self):
        """Тест строкового отображения"""

        self.assertEqual(
            str(self.orders),
            f"Guest: {self.orders.user}, table: №{self.orders.table}, time exp.: {self.orders.expired_time}",
        )


class UserTest(TestCase, TestMaxLengthMixin, TestVerboseNameMixin):
    @classmethod
    def setUpTestData(cls) -> None:
        """Заносит данные в БД перед запуском тестов класса"""

        cls.users = UserModel.objects.create(name="test_name", phone="+79098654412")
        cls.field_and_max_length = {"name": 200}
        cls.field_and_verbose_name = {"name": "Имя", "phone": "Телефон"}
        cls.name = cls.users._meta.get_field("name")
        cls.phone = cls.users._meta.get_field("phone")

    def test_user_name_max_length(self):
        """Тест параметра max_length"""

        super().run_max_length_test(UserModel)

    def test_user_verbose_names(self):
        """Тест параметра verbose_name"""

        super().run_verbose_name_test(UserModel)

    def test_unique(self):
        """Тест параметра unique"""

        real_unique = getattr(self.phone, "unique")

        self.assertTrue(real_unique)

    def test_str_method(self):
        """Тест строкового отображения"""

        self.assertEqual(
            str(self.users),
            f"Имя пользователя: {self.users.name}. Телефон: {self.users.phone}",
        )
