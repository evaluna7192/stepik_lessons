# Data
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
add_to_basket_button_locator = ".btn-add-to-basket"
add_to_basket_button_text_locator = ".btn-add-to-basket"
basket_button_text_dict = {'en-GB': 'Add to basket',
                           'ru': 'Добавить в корзину',
                           'es': 'Añadir al carrito',
                           'fr': 'Ajouter au panier'}


def test_add_to_basket_button_is_presented(browser, site_language):
    # Arrange
    browser.get(link)
    browser.implicitly_wait(10)

    # Act
    add_to_basket_button = browser.find_element_by_css_selector(add_to_basket_button_locator)
    add_to_basket_button_text = browser.find_element_by_css_selector(add_to_basket_button_text_locator)
    text_from_dict_for_basket_button = basket_button_text_dict.get(site_language)

    # Assert
    assert add_to_basket_button, \
        "Page does not have an add to basket button"
    assert add_to_basket_button_text.text == text_from_dict_for_basket_button, \
        f"Page have incorrect text of Add to basket button for {site_language}"
