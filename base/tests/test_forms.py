from django.test import TestCase

from base.forms import MyUserCreationForm, MenuForm, GamesForm, OrdersForm


class UserFormTests(TestCase):
    """Тесты формы MyUserCreationForm"""

    def test_field_labels(self):
        """Тест лейблов полей"""

        form = MyUserCreationForm()
        name_label = form.fields['name'].label
        phone_label = form.fields['phone'].label

        self.assertEqual(name_label, 'Имя')
        self.assertEqual(phone_label, 'Телефон')


class MenuFormTests(TestCase):
    """Тесты формы MenuForm"""

    def test_field_labels(self):
        """Тест лейблов полей"""

        form = MenuForm()
        product_name_label = form.fields['product_name'].label
        
        self.assertEqual(product_name_label, 'Наименование продукта')


class GamesFormTests(TestCase):
    """Тесты формы GamesForm"""

    def test_field_labels(self):
        """Тест лейблов полей"""

        form = GamesForm()
        game_name_label = form.fields['game_name'].label
        
        self.assertEqual(game_name_label, 'Название игры')


