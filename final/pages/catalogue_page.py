from .base_page import BasePage
from .locators import CataloguePageLocators


class CataloguePage(BasePage):
    def should_be_correct_page_of_catalogue(self, page_number):
        catalogue_page = self.browser.find_element(*CataloguePageLocators.CATALOGUE_PAGE_LOCATOR)
        assert page_number in catalogue_page.text, "Page number is not correct"
