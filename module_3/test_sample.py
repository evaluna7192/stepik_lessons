from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

email_field_locator = "[name = 'registration-email']"
password_locator = "[name = 'registration-password1']"
confirm_password_locator = "[name = 'registration-password2']"
register_button_locator = "[name = 'registration_submit']"
account_button_locator = "i.icon-user"
logout_button_locator = "#logout_link"


def test_register_new_user():
    # Data
    email = str(time.time()) + "@fakemail.org"
    password = "Expired_2"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_page_link)
        registration_message_text = "Спасибо за регистрацию!"

        # Act
        email_field = browser.find_element_by_css_selector(email_field_locator)
        email_field.send_keys(email)
        password_field = browser.find_element_by_css_selector(password_locator)
        password_field.send_keys(password)
        confirm_password_field = browser.find_element_by_css_selector(confirm_password_locator)
        confirm_password_field.send_keys(password)
        register_button = browser.find_element_by_css_selector(register_button_locator)
        register_button.click()

        # Assert
        registration_message = WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.wicon")))
        assert registration_message_text in registration_message.text, \
            "Successful message about registration is not presented"
        assert browser.current_url == main_page_link, \
            "Redirection is not on main page"
        account_button = browser.find_element_by_css_selector(account_button_locator)
        assert account_button, \
            "Account icon is not  presented"
        logout_button = browser.find_element_by_css_selector(logout_button_locator)
        assert logout_button, \
            "Logout button is not presented"
    finally:
        time.sleep(5)
        browser.quit()


test_register_new_user()
