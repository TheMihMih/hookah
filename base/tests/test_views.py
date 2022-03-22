from django.test import TestCase
from re import findall

from requests import head, get



DOMAIN = 'http://127.0.0.1:8000'

PAGES = (
    '/',
    '/map',
    '/check_reservations',
    '/games/8',
    '/games',
    '/menu',
    '/make_order/3'

)

PAGES = (DOMAIN + page for page in PAGES)

LINK_REGULAR_EXPRESSION = r'<a[^>]* href="([^"]*)"'


def get_full_link(link: str) -> str:
    """Возвращает полную ссылку (с URL-адресом сайта)"""

    if not link.startswith('http'):
        link = DOMAIN + link

    return link


class PagesTests(TestCase):
    """Класс с тестами страниц"""

    def test_status_code(self):
        """Тест статус-кода"""

        for page in PAGES:
            with self.subTest(f'{page=}'):

                response = get(page)

                self.assertEqual(response.status_code, 200)


    def test_links(self):
        """Тест ссылок страниц"""

        valid_links = set()

        for page in PAGES:
            page_content = get(page).content # (1)
            page_links = set( # (2)
                findall(LINK_REGULAR_EXPRESSION, str(page_content))
            )

            for link in page_links:
                link = get_full_link(link)

                with self.subTest(f'{link=} | {page=}'):
                    response = head(link, allow_redirects=True)

                    if response.status_code == 200:
                        valid_links.add(link)

                    self.assertEqual(response.status_code, 200) # (3)
