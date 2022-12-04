import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

import pytest

from page_objects.admin_product_page import AdminProductPage
from test_data.get_data_from_excel import GetTestData

get_data = GetTestData()
success_create_product_data = get_data.get_success_create_product_data()
failed_create_product_data = get_data.get_failed_create_product_data()

# Test case 1 : Create Product Success (3 Test Cases)
# Given login success
# When create product with valid values (According to Stylish-Test Case.xlsx - "Create Product Success" sheet)
# Then alert message "Create Product Success" should be shown
# And new product should be displayed on product list
@pytest.mark.parametrize('success_create_product_data', success_create_product_data)
def test_create_product_success(driver, member_browser, success_create_product_data):
    LOGGER.info("[START] test_create_product_success")

    member_browser.load_page("admin/products.html")
    LOGGER.info("[PAGE] Switch to admin product page")

    admin_product_page = AdminProductPage(driver)
    admin_product_page.click_create_new_product_btn()
    LOGGER.info("[ACTION] Click create new product button")

    admin_product_page.switch_to_the_page("product creation page")
    LOGGER.info("[PAGE] Switch to admin product creation page")

    admin_product_page.input_product_data(success_create_product_data)
    LOGGER.info("[ACTION] Input product data")

    admin_product_page.click_create_product_btn()
    LOGGER.info("[ACTION] Click create product button")

    assert admin_product_page.alert_is_present().text == "Create Product Success"
    LOGGER.info("[VERIFICATION] Alert message 'Create Product Success' should be shown")

    admin_product_page.alert_is_present().accept()
    LOGGER.info("[UI] Accept alert")

    admin_product_page.switch_to_the_page("product list page")
    LOGGER.info("[PAGE] Switch back to admin product page")

    admin_product_page.driver.refresh()
    LOGGER.info("[ACTION] Refresh on the product page")

    assert success_create_product_data["Title"] in admin_product_page.check_product_creation()
    LOGGER.info("[VERIFICATION] New product should be displayed on product list")

    admin_product_page.delete_product(success_create_product_data["Title"])
    LOGGER.info(f"[ACTION] Delete product: {success_create_product_data['Title']}")

    admin_product_page.alert_is_present().accept()
    LOGGER.info("[UI] This alert accept is for Selenium screenshot, accept alert")

    LOGGER.info("[END] test_create_product_success")

# Test case 2 : Create Product with Invalid Value (20 Test Cases)
# Given login success
# When create product with valid values (According to Stylish-Test Case.xlsx - "Create Product Failed" sheet)
# Then related alert message should be shown
@pytest.mark.parametrize('failed_create_product_data', failed_create_product_data)
def test_create_product_failed(driver, member_browser, failed_create_product_data):
    LOGGER.info("[START] test_create_product_failed")

    member_browser.load_page("admin/products.html")
    LOGGER.info("[PAGE] Switch to admin product page")

    admin_product_page = AdminProductPage(driver)
    admin_product_page.click_create_new_product_btn()
    LOGGER.info("[ACTION] Click create new product button")

    admin_product_page.switch_to_the_page("product creation page")
    LOGGER.info("[PAGE] Switch to admin product creation page")

    admin_product_page.input_product_data(failed_create_product_data)
    LOGGER.info("[ACTION] Input product data")

    admin_product_page.click_create_product_btn()
    LOGGER.info("[ACTION] Click create product button")

    assert admin_product_page.alert_is_present().text == failed_create_product_data["Alert Msg"]
    LOGGER.info("[VERIFICATION] Related alert message should be shown")

    admin_product_page.alert_is_present().accept()
    LOGGER.info("[UI] Accept alert")

    LOGGER.info("[END] test_create_product_failed")

# Test case 3 : Create Product without login
# Given create product with valid values
# Then alert message "Please Login first" should be shown
# And should be redirected to login page
def test_create_product_without_login(driver):
    LOGGER.info("[START] test_create_product_without_login")

    admin_product_page = AdminProductPage(driver)
    admin_product_page.load_page("admin/product_create.html")

    admin_product_page.click_create_product_btn()
    assert admin_product_page.alert_is_present().text == "Please Login First"
    admin_product_page.alert_is_present().accept()
    
    assert driver.current_url == env["UAT_URL"] + "login.html"

    LOGGER.info("[END] test_create_product_without_login")