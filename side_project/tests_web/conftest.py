import pytest
import allure

import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

from sql_objects.product import Product

from page_objects.product_page import ProductPage
from page_objects.member_page import MemberPage

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def main_browser():
    options = Options()
    options.chrome_executable_path = env["CHROME_EXECUTABLE_PATH"]
    driver = webdriver.Chrome(options = options)
    driver.maximize_window()
    driver.get(env['UAT_URL'])
    LOGGER.info("[PAGE] Enter to main page")

    yield driver
    
    allure.attach(driver.get_screenshot_as_png(), name = "Screenshot", attachment_type = allure.attachment_type.PNG)
    driver.quit()

@pytest.fixture()
def get_product():
    product_sql = Product()
    product = product_sql.get_a_product_randomly()
    LOGGER.info(f"[DB] Profuct info: {product}")

    return product

@pytest.fixture()
def product_browser(main_browser, get_product):
    product_page = ProductPage(main_browser)
    product_page.input_search_text(get_product[1])
    product_page.click_product(get_product[0])
    LOGGER.info("[PAGE] Switch to product page")

    return product_page

@pytest.fixture()
def member_browser(main_browser):
    email = env["UAT_ACCOUNT"]
    password = env["UAT_PASSWORD"]

    member_page = MemberPage(main_browser)
    member_page.click_profile_btn()
    LOGGER.info("[PAGE] Switch to login page")

    member_page.log_in(email, password)
    LOGGER.info(f"[ACTION] Log in as {email}")

    assert member_page.alert_is_present().text == "Login Success"
    LOGGER.info("[VERIFICATION] Log in successfully")

    LOGGER.info("[PAGE] Switch to profile page")

    member_page.alert_is_present().accept()
    LOGGER.info("[ACTION] Click confirm btn")

    return member_page