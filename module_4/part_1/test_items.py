import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
add_to_basket_button_locator = ".btn-add-to-basket"


def test_add_to_basket_button_is_presented(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    time.sleep(5)

    add_to_basket_button = browser.find_element_by_css_selector(add_to_basket_button_locator)
    assert add_to_basket_button, \
        "Page does not have an add to basket button"
