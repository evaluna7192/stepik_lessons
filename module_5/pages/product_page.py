from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_product_in_basket(self):
        self.should_be_correct_name_of_product()
        self.should_be_correct_price_of_product()

    def should_be_correct_name_of_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        correct_product_name = self.browser.find_element(*ProductPageLocators.CORRECT_PRODUCT_NAME).text
        assert product_name == correct_product_name, "Product name is not correct"

    def should_be_correct_price_of_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        correct_product_price = self.browser.find_element(*ProductPageLocators.CORRECT_PRODUCT_PRICE).text
        assert product_price == correct_product_price, "Product price is not correct"
