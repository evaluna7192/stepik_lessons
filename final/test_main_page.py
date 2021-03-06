from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

# Data
link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу

        # Act
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_page()  # проверяем что url верный и есть формы логина и регистрации

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Assert
        page.should_be_login_link()


class TestMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.should_be_empty_basket()


@pytest.mark.personal_tests
class TestAuthorizedUserFromMainPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Data
        email = str(time.time()) + "@wrongmail.org"
        password = "Qwaszx@123"

        # Arrange
        page = LoginPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        page.register_new_user(email, password)

        # Assert
        page.should_be_authorized_user()

    def test_user_can_logout(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.logout()

        # Assert
        page.should_be_login_link()

    def test_user_can_open_account_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.go_to_account_page()

        # Assert
        page.should_be_account_page()

    def test_user_can_not_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Assert
        page.should_not_be_login_link()
