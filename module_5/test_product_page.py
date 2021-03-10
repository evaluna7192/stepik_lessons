from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

# Data
link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
email = str(time.time()) + "@fakemail.org"
password = "Qwaszx@123"


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Arrange
        product_link = f"{link1}/?promo={promo_offer}"
        page = ProductPage(browser, product_link)
        page.open()

        # Act
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_be_correct_product_in_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link1)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link1)
        page.open()

        # Assert
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link1)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.should_disappear_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link2)
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link2)
        page.open()

        # Act
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link1)
        page.open()

        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.should_be_empty_basket()


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Arrange
        page = LoginPage(browser, link1)
        page.open()

        # Act
        page.go_to_login_page()
        page.register_new_user(email, password)

        # Assert
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link1)
        page.open()

        # Assert
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link1)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.should_be_correct_product_in_basket()
