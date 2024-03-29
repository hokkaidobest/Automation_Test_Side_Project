import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

import pytest

from sql_objects.product import Product
from page_objects.product_page import ProductPage

@pytest.fixture()
def get_product():
    product_sql = Product()
    product = product_sql.get_a_product_randomly()
    LOGGER.info(f"[DB] Profuct info: {product}")

    return product

# Test case 1 : Color Selection 
# Given entered a product page
# When select a color of the product
# Then selected color is highlighted
def test_color_selection(driver, get_product):
    LOGGER.info("[START] test_color_selection")
    
    product_page = ProductPage(driver)
    product_page.input_search_text(get_product['title'])
    product_page.click_product(get_product['id'])
    LOGGER.info("[PAGE] Switch to product page")

    colors = product_page.get_color()
    LOGGER.info(f"[UI] Profuct colors: {colors}")

    for color in colors:
        color.click()
        LOGGER.info("[ACTION] Click color btn")

        selected_color = product_page.get_selected_color()
        selected_color_id = selected_color.get_attribute("data_id")
        selected_color_class = selected_color.get_attribute("class")
        LOGGER.info(f"[UI] Color selected {selected_color_id}, {selected_color_class}")
        
        assert "product__color--selected" in selected_color_class
        LOGGER.info("[VERIFICATION] Selected color is highlighted")
        LOGGER.info("[END] test_color_selection")

# Test case 2 : Size Selection
# Given entered a product page
# When select a size of the product
# Then selected size is highlighted
def test_size_selection(driver, get_product):
    LOGGER.info("[START] test_size_selection")

    product_page = ProductPage(driver)
    product_page.input_search_text(get_product['title'])
    product_page.click_product(get_product['id'])
    LOGGER.info("[PAGE] Switch to product page")

    sizes = product_page.get_size()
    LOGGER.info(f"[UI] Product sizes: {sizes}")

    for size in sizes:
        size.click()
        LOGGER.info("[ACTION] Select a size of the product")

        selected_size_class = size.get_attribute("class")
        LOGGER.info(f"[UI] Size selected {selected_size_class}")

        assert "product__size product__size--selected" in selected_size_class
        LOGGER.info("[VERIFICATION] Selected size is highlighted")
        LOGGER.info("[END] test_size_selection")

# Test case 3 : Quantity Editor Disabled
# Given entered a product page
# When edit quantity without size selection
# Then quantity editor is disabled
def test_quantity_editor_disabled(driver, get_product):
    LOGGER.info("[START] test_quantity_editor_disabled")

    product_page = ProductPage(driver)
    product_page.input_search_text(get_product['title'])
    product_page.click_product(get_product['id'])
    LOGGER.info("[PAGE] Switch to product page")

    # Click add quantity btn once
    product_page.click_add_quantity_btn(1)
    LOGGER.info("[ACTION] Click add quantity btn once")

    assert product_page.get_current_quantity_value() == "1"
    LOGGER.info("[VERIFICATION] Quantity editor is disabled")
    LOGGER.info("[END] test_size_selection")

# Test case 4 : Quantity Editor - Increase Quantity
# Given entered a product page
# And select a size of the product
# When add 8 more quantity
# Then quantity should be 9
# When add 2 more quantity
# Then quantity still be 9
def test_increase_quantity(driver, get_product):
    LOGGER.info("[START] test_increase_quantity")

    product_page = ProductPage(driver)
    product_page.input_search_text(get_product['title'])
    product_page.click_product(get_product['id'])
    LOGGER.info("[PAGE] Switch to product page")

    # Click first size btn of product
    product_page.click_size_btn()
    LOGGER.info("[ACTION] Click size btn")

    product_page.click_add_quantity_btn(8)
    LOGGER.info("[ACTION] add 8 more quantity")

    assert product_page.get_current_quantity_value() == "9"
    LOGGER.info("[VERIFICATION] Quantity should be 9")

    product_page.click_add_quantity_btn(2)
    LOGGER.info("[ACTION] Add 2 more quantity")

    assert product_page.get_current_quantity_value() == "9"
    LOGGER.info("[VERIFICATION] Quantity still be 9")
    LOGGER.info("[END] test_increase_quantity")

# Test case 5 : Quantity Editor - Decrease Quantity
# Given entered a product page
# And select a size of the product
# And add 8 more quantity
# When decrease 8 quantity
# Then quantity should be 1
def test_decrease_quantity(driver, get_product):
    LOGGER.info("[START] test_decrease_quantity")

    product_page = ProductPage(driver)
    product_page.input_search_text(get_product['title'])
    product_page.click_product(get_product['id'])
    LOGGER.info("[PAGE] Switch to product page")

    # Click first size btn of product
    product_page.click_size_btn()
    LOGGER.info("[ACTION] Click size btn")
    
    product_page.click_add_quantity_btn(8)
    LOGGER.info("[ACTION] Click add quantity btn 8 times")

    product_page.click_minus_quantity_btn(8)
    LOGGER.info("[ACTION] Click minus quantity btn 8 times")

    assert product_page.get_current_quantity_value() == "1"
    LOGGER.info("[VERIFICATION] Quantity should be 1")
    LOGGER.info("[END] test_decrease_quantity")

# Test case 6 : Add To Cart - Success
# Given entered a product page
# And select a size of the product
# When click add to cart button
# Then success message should be shown
# And cart icon number should be 1
def test_add_to_cart_success(driver, get_product):
    LOGGER.info("[START] test_add_to_cart_success")

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
    LOGGER.info("[END] test_add_to_cart_success")

# Test case 7 : Add To Cart - Failed
# Given entered a product page without size selection
# When click add to cart button
# Then alert message should be shown
def test_add_to_cart_failed(driver, get_product):
    LOGGER.info("[START] test_add_to_cart_failed")

    product_page = ProductPage(driver)
    product_page.input_search_text(get_product['title'])
    product_page.click_product(get_product['id'])
    LOGGER.info("[PAGE] Switch to product page")

    product_page.click_add_to_cart_btn()
    LOGGER.info("[ACTION] Click add to cart btn")

    assert product_page.alert_is_present().text == "請選擇尺寸" 
    LOGGER.info("[VERIFICATION] Alert message should be shown")

    product_page.alert_is_present().accept()
    LOGGER.info("[ACTION] Accept alert for screenshot")

    LOGGER.info("[END] test_add_to_cart_failed")