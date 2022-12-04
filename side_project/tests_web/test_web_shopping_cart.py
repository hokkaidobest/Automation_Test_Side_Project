import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

import pytest
import random

from sql_objects.product import Product
from page_objects.cart_page import CartPage
from page_objects.product_page import ProductPage

@pytest.fixture()
def get_product():
    product_sql = Product()
    product = product_sql.get_a_product_randomly()
    LOGGER.info(f"[DB] Profuct info: {product}")

    return product

# Test case 1 : Shopping Cart Info Correct
# When add product to shopping cart
# Then cart info is displayed correctly
def test_shopping_cart_info_correct(driver, get_product):
    LOGGER.info("[START] test_shopping_cart_info_correct")

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

    selected_product = product_page.get_selected_product_info()
    LOGGER.info(f"[DATA] The selected product info: {selected_product}")

    product_page.load_page("cart.html")
    LOGGER.info("[PAGE] Switch to cart page")
    
    cart_page = CartPage(driver)
    cart_item = cart_page.get_cart_item_info()
    LOGGER.info(f"[DATA] The cart item info {cart_item}")

    assert selected_product["id"] == cart_item["id"]
    assert selected_product["title"] == cart_item["title"]
    assert selected_product["color"] == cart_item["color"]
    assert selected_product["size"] == cart_item["size"] 
    assert selected_product["quantity"] == cart_item["quantity"]
    assert selected_product["price"] == cart_item["price"]
    assert selected_product["sub_total"] == cart_item["sub_total"]
    assert cart_page.get_cart_number() == "1"
    LOGGER.info("[VERIFICATION] Cart icon number should be 1")

    LOGGER.info("[END] test_shopping_cart_info_correct")

# Test case 2 : Remove product from cart
# Given add 2 products to shopping cart
# When delete product from shopping cart
# Then alert message "已刪除商品" should be shown
# And new cart info should be updated correctly
# And cart icon number should be updated correctly
def test_remove_product_from_cart(driver, get_product):
    LOGGER.info("[START] test_remove_product_from_cart")

    products_number_count = 2

    for _ in range(products_number_count):
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

        selected_product = product_page.get_selected_product_info()
        LOGGER.info(f"[DATA] The selected product info: {selected_product}")

        product_page.load_page("cart.html")
        LOGGER.info("[PAGE] Switch to cart page")
    
    assert product_page.get_cart_number() == "2"
    LOGGER.info("[VERIFICATION] Cart icon number should be 2")

    cart_page = CartPage(driver)
    cart_page.delect_item()
    assert cart_page.alert_is_present().text == "已刪除商品"
    LOGGER.info("[VERIFICATION] alert message '已刪除商品' should be shown")
    cart_page.alert_is_present().accept()
    
    cart_item = cart_page.get_cart_item_info()
    LOGGER.info(f"[DATA] The cart item info {cart_item}")

    assert selected_product["id"] == cart_item["id"]
    assert selected_product["title"] == cart_item["title"]
    assert selected_product["color"] == cart_item["color"]
    assert selected_product["size"] == cart_item["size"] 
    assert selected_product["quantity"] == cart_item["quantity"]
    assert selected_product["price"] == cart_item["price"]
    assert selected_product["sub_total"] == cart_item["sub_total"]
    assert cart_page.get_cart_number() == "1"
    LOGGER.info("[VERIFICATION] Cart icon number should be 1")

    LOGGER.info("[END] test_remove_product_from_cart")

# Test case 3 : Edit quantity in cart
# Given product added to shopping cart
# When edit the quantity of the product
# Then alert message "已修改數量" should be shown
# And subtotal should be updated correctly
def test_edit_quantity_in_cart(driver, get_product):
    LOGGER.info("[START] test_edit_quantity_in_cart")

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

    new_quantity = random.randint(1, 8)
    cart_page.edit_item_quantity(new_quantity)
    LOGGER.info(f"[DATA] Edit the cart item's quantity to {new_quantity + 1}")

    assert cart_page.alert_is_present().text == "已修改數量"
    LOGGER.info("[VERIFICATION] Alert message '已修改數量' should be shown")
    cart_page.alert_is_present().accept()

    new_sub_total = cart_item["price"] * (new_quantity + 1)
    LOGGER.info(f"[DATA] Count the new sub_total of item is: {new_sub_total}")

    assert new_sub_total == cart_page.get_edit_sub_total()
    LOGGER.info("[VERIFICATION] Subtotal should be updated correctly")

    LOGGER.info("[END] test_edit_quantity_in_cart")