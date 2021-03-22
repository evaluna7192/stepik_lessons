from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators
import pytest

# Data
main_page = "http://selenium1py.pythonanywhere.com"
main_page_header_text = "Welcome!"


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        # Act
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        # Assert
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        # Act
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_authorized_user(self):
        # Assert
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def logout(self):
        # Act
        logout_link = self.browser.find_element(*BasePageLocators.LOGOUT_LINK)
        logout_link.click()

    def go_to_main_page(self):
        # Act
        main_page_link = self.browser.find_element(*BasePageLocators.MAIN_PAGE_LINK)
        main_page_link.click()

    def should_be_main_page(self):
        self.should_be_main_url()
        self.should_be_main_page_header()

    def should_be_main_url(self, site_language):
        main_page_link = f"{main_page}/{site_language}"
        assert main_page_link == self.browser.current_url, "Main page url is npt correct"

    def should_be_main_page_header(self):
        main_page_header = self.browser.find_element(*BasePageLocators.MAIN_PAGE_HEADER)
        assert main_page_header_text == main_page_header.text, \
            "There is no main page header, there is not main page probably"

    def go_to_account_page(self):
        # Act
        account_link = self.browser.find_element(*BasePageLocators.ACCOUNT_LINK)
        account_link.click()

    def should_be_account_page(self):
        # Assert
        assert "accounts" in self.browser.current_url, \
            "Account page url is not correct"
