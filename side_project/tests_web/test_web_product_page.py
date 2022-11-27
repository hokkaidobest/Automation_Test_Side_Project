import logging

from page_objects.product_page import ProductPage
from sql_objects.product import Product

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

# Test case 1 : Color Selection 
# Given entered a product page
# When select a color of the product
# Then selected color is highlighted
def test_color_selection(product_broswer):
    LOGGER.info("[START] test_color_selection")
    LOGGER.info("[PAGE] Enter main page")

    colors = product_broswer.get_color()
    LOGGER.info(f"[UI] Profuct colors: {colors}")

    for color in colors:
        color.click()
        LOGGER.info("[ACTION]] Click color btn")

        selected_color = product_broswer.get_selected_color()
        selected_color_id = selected_color.get_attribute("data_id")
        selected_color_class = selected_color.get_attribute("class")
        LOGGER.info(f"[UI] Color selected {selected_color_id}, {selected_color_class}")
        
        assert "product__color--selected" in selected_color_class
        LOGGER.info(f"[VERIFICATION] Selected color is highlighted")
        LOGGER.info(f"[END] test_color_selection")

# Test case 2 : Size Selection
# Given entered a product page
# When select a size of the product
# Then selected size is highlighted
def test_size_selection(product_broswer):
    LOGGER.info("[START] test_size_selection")
    LOGGER.info("[PAGE] Enter main page")

    sizes = product_broswer.get_size()
    LOGGER.info(f"[UI] Profuct sizes: {sizes}")

    for size in sizes:
        size.click()
        LOGGER.info("[ACTION]] Select a size of the product")

        selected_size_class = size.get_attribute("class")
        LOGGER.info(f"[UI] Size selected {selected_size_class}")

        assert "product__size product__size--selected" in selected_size_class
        LOGGER.info(f"[VERIFICATION] Selected size is highlighted")
        LOGGER.info(f"[END] test_size_selection")

# Test case 3 : Quantity Editor Disabled
# Given entered a product page
# When edit quantity without size selection
# Then quantity editor is disabled
def test_quantity_editor_disabled(product_broswer):
    LOGGER.info("[START] test_quantity_editor_disabled")
    LOGGER.info("[PAGE] Enter main page")

    # Click add quantity btn once
    product_broswer.click_add_quantity_btn(1)
    LOGGER.info("[ACTION]] Click add quantity btn once")

    assert product_broswer.get_current_quantity_value() == "1"
    LOGGER.info(f"[VERIFICATION] Quantity editor is disabled")
    LOGGER.info(f"[END] test_size_selection")

# Test case 4 : Quantity Editor - Increase Quantity
# Given entered a product page
# And select a size of the product
# When add 8 more quantity
# Then quantity should be 9
# When add 2 more quantity
# Then quantity still be 9
def test_increase_quantity(product_broswer):
    LOGGER.info("[START] test_increase_quantity")
    LOGGER.info("[PAGE] Enter main page")

    # Click first size btn of product
    product_broswer.click_size_btn()
    LOGGER.info("[ACTION]] Click size btn")

    product_broswer.click_add_quantity_btn(8)
    LOGGER.info("[ACTION]] add 8 more quantity")

    assert product_broswer.get_current_quantity_value() == "9"
    LOGGER.info(f"[VERIFICATION] Quantity should be 9")

    product_broswer.click_add_quantity_btn(2)
    LOGGER.info("[ACTION]] Add 2 more quantity")

    assert product_broswer.get_current_quantity_value() == "9"
    LOGGER.info(f"[VERIFICATION] Quantity still be 9")
    LOGGER.info(f"[END] test_increase_quantity")

# Test case 5 : Quantity Editor - Decrease Quantity
# Given entered a product page
# And select a size of the product
# And add 8 more quantity
# When decrease 8 quantity
# Then quantity should be 1
def test_decrease_quantity(product_broswer):
    LOGGER.info("[START] test_decrease_quantity")
    LOGGER.info("[PAGE] Enter main page")

    # Click first size btn of product
    product_broswer.click_size_btn()
    LOGGER.info("[ACTION]] Click size btn")
    
    product_broswer.click_add_quantity_btn(8)
    LOGGER.info("[ACTION]] Click add quantity btn 8 times")

    product_broswer.click_minus_quantity_btn(8)
    LOGGER.info("[ACTION]] Click minus quantity btn 8 times")

    assert product_broswer.get_current_quantity_value() == "1"
    LOGGER.info(f"[VERIFICATION] Quantity should be 1")
    LOGGER.info(f"[END] test_decrease_quantity")

# Test case 6 : Add To Cart - Success
# Given entered a product page
# And select a size of the product
# When click add to cart button
# Then success message should be shown
# And cart icon number should be 1
def test_add_to_cart_success(product_broswer):
    LOGGER.info("[START] test_add_to_cart_success")
    LOGGER.info("[PAGE] Enter main page")

    product_broswer.click_size_btn()
    LOGGER.info("[ACTION]] Click size btn")

    product_broswer.click_add_to_cart_btn()
    LOGGER.info("[ACTION]] Click add to cart btn")

    product_broswer.alert_is_present().accept()
    LOGGER.info("[UI]] Accept alert")

    assert product_broswer.get_cart_number() == "1"
    LOGGER.info(f"[VERIFICATION] Cart icon number should be 1")
    LOGGER.info(f"[END] test_add_to_cart_success")

# Test case 7 : Add To Cart - Failed
# Given entered a product page without size selection
# When click add to cart button
# Then alert message should be shown
def test_add_to_cart_failed(product_broswer):
    LOGGER.info("[START] test_add_to_cart_failed")
    LOGGER.info("[PAGE] Enter main page")

    product_broswer.click_add_to_cart_btn()
    LOGGER.info("[ACTION]] Click add to cart btn")

    assert product_broswer.alert_is_present().text == "請選擇尺寸" 
    LOGGER.info(f"[VERIFICATION] Alert message should be shown")
    LOGGER.info(f"[END] test_add_to_cart_failed")