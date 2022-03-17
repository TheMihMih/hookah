from django.test import TestCase

from base.forms import MyUserCreationForm, MenuForm, GamesForm, OrdersForm


class UserFormTests(TestCase):
    """Тесты формы TrialForm"""

    def test_field_labels(self):
        """Тест лейблов полей"""

        form = MyUserCreationForm()
        name_label = form.fields['name'].label

        self.assertEqual(name_label, 'Name')