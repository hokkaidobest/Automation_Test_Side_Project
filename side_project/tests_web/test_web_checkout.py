import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

import pytest

from sql_objects.product import Product
from page_objects.cart_page import CartPage
from page_objects.product_page import ProductPage
from test_data.get_data_from_excel import GetTestData

get_data = GetTestData()
invalid_checkout_data = get_data.get_invalid_checkout_data()
valid_checkout_data = get_data.get_valid_checkout_data()

@pytest.fixture()
def get_product():
    product_sql = Product()
    product = product_sql.get_a_product_randomly()
    LOGGER.info(f"[DB] Profuct info: {product}")

    return product

# Test case 1 : Checkout with empty cart
# When click checkout button without add product to shopping cart
# Then alert message "尚未選購商品" should be shown
def test_checkout_with_empty_cart(driver, member_browser):
    LOGGER.info("[START] test_checkout_with_empty_cart")

    member_browser.load_page("cart.html")
    LOGGER.info("[PAGE] Switch to cart page")

    cart_page = CartPage(driver)
    cart_page.click_checkout_btn()
    LOGGER.info("[ACTION] Click checkout button without add product to shopping cart")

    assert cart_page.alert_is_present().text == "尚未選購商品"
    LOGGER.info("[VERIFICATION] Cart icon number should be 1")

    cart_page.alert_is_present().accept()
    LOGGER.info("[UI] Accept alert")

    LOGGER.info("[END] test_checkout_with_empty_cart")

# Test case 2 : Checkout with invalid values (17 Test Cases)
# Given login success
# And add product to shopping cart
# When checkout with invalid value (According to Stylish-Test Case.xlsx - "Checkout with Invalid Value" sheet)
# Then related alert message should be shown
@pytest.mark.parametrize('invalid_checkout_data', invalid_checkout_data)
def test_checkout_with_invalid_values(driver, member_browser, get_product, invalid_checkout_data):
    LOGGER.info("[START] test_checkout_with_invalid_values")

    product_page = ProductPage(driver)
    product_page.input_search_text(get_product['title'])
    product_page.click_product(get_product['id'])
    LOGGER.info("[PAGE] Switch to product page")

    product_page.click_size_btn()
    LOGGER.info("[ACTION] Click size btn")

    product_page.click_add_to_cart_btn()
    LOGGER.info("[ACTION] Click add to cart btn")

    product_page.alert_is_present().accept()
    LOGGER.info("[UI] Accept alert")

    assert product_page.get_cart_number() == "1"
    LOGGER.info("[VERIFICATION] Cart icon number should be 1")

    product_page.load_page("cart.html")
    LOGGER.info("[PAGE] Switch to cart page")

    cart_page = CartPage(driver)
    cart_page.input_checkout_info(invalid_checkout_data)
    LOGGER.info("[ACTION] Input checkout info")

    cart_page.click_checkout_btn()
    LOGGER.info("[ACTION] Click checkout button without add product to shopping cart")

    assert cart_page.alert_is_present().text == invalid_checkout_data["Alert Msg"]
    LOGGER.info("[VERIFICATION] Related alert message should be shown")

    cart_page.alert_is_present().accept()
    LOGGER.info("[UI] Accept alert")

    LOGGER.info("[END] test_checkout_with_invalid_values")

# Test case 3 : Checkout with valid values (3 Test Cases)
# Given login success
# And add product to shopping cart
# When checkout with valid value (According to Stylish-Test Case.xlsx - "Checkout with Valid Value" sheet)
# Then alert message "付款成功" should be shown
# And correct order info should be displayed in thankyou page
@pytest.mark.parametrize('valid_checkout_data', valid_checkout_data)
def test_checkout_with_valid_values(driver, member_browser, get_product, valid_checkout_data):
    LOGGER.info("[START] test_checkout_with_valid_values")

    product_page = ProductPage(driver)
    product_page.input_search_text(get_product['title'])
    product_page.click_product(get_product['id'])
    LOGGER.info("[PAGE] Switch to product page")

    product_page.click_size_btn()
    LOGGER.info("[ACTION] Click size btn")

    product_page.click_add_to_cart_btn()
    LOGGER.info("[ACTION] Click add to cart btn")

    product_page.alert_is_present().accept()
    LOGGER.info("[UI] Accept alert")

    assert product_page.get_cart_number() == "1"
    LOGGER.info("[VERIFICATION] Cart icon number should be 1")

    product_page.load_page("cart.html")
    LOGGER.info("[PAGE] Switch to cart page")

    cart_page = CartPage(driver)

    cart_item = cart_page.get_cart_item_info()
    LOGGER.info(f"[DATA] The cart item info {cart_item}")

    cart_page.input_checkout_info(valid_checkout_data)
    LOGGER.info("[ACTION] Input checkout info")

    order_info = {
        "amount_payable": int(cart_item["sub_total"]) + 30,
        "Receiver": valid_checkout_data["Receiver"],
        "Email": valid_checkout_data["Email"],
        "Mobile": valid_checkout_data["Mobile"],
        "Address": valid_checkout_data["Address"],
        "Deliver Time": valid_checkout_data["Deliver Time"]
    }

    cart_page.click_checkout_btn()
    LOGGER.info("[ACTION] Click checkout button without add product to shopping cart")

    assert cart_page.alert_is_present().text == "付款成功"
    LOGGER.info("[VERIFICATION] Alert message '付款成功' should be shown")

    cart_page.alert_is_present().accept()
    LOGGER.info("[UI] Accept alert")

    cart_item.update(order_info)
    LOGGER.info(f"[DATA] The checkout data include item and receiver: {cart_item}")

    order = cart_page.get_order_product_info()
    order.update(cart_page.get_order_recipient_info())
    LOGGER.info(f"[DATA] The order data include item and receiver: {order}")

    assert cart_item == order
    LOGGER.info("[VERIFICATION] Correct order info should be displayed in thankyou page")

    LOGGER.info("[END] test_checkout_with_valid_values")