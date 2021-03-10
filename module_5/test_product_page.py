from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        product_link = f"{link1}/?promo={promo_offer}"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_correct_product_in_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.add_product_to_basket()
        page.should_disappear_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link2)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link2)
        page.open()
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
