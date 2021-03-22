from .pages.catalogue_page import CataloguePage
import pytest

# Data
link = "http://selenium1py.pythonanywhere.com/catalogue/"


class TestCataloguePage():
    @pytest.mark.personal_tests
    @pytest.mark.parametrize('page_number',
                             ["2", "3"])
    def test_guest_can_go_to_different_catalogue_pages(self, browser, page_number):
        # Act
        catalogue_link = f"{link}/?page={page_number}"
        page = CataloguePage(browser, catalogue_link)
        page.open()

        # Assert
        page.should_be_correct_page_of_catalogue(page_number)
