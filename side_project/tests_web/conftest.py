import pytest
import allure

import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

from page_objects.member_page import MemberPage
from page_objects.prime_page import PrimePage

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def driver():
    options = Options()
    options.chrome_executable_path = env["CHROME_EXECUTABLE_PATH"]
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    service = Service(executable_path = ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service, options = options)
    driver.maximize_window()
    driver.get(env['UAT_URL'])
    LOGGER.info("[PAGE] Enter to main page")

    yield driver
    
    allure.attach(driver.get_screenshot_as_png(), name = "Screenshot", attachment_type = allure.attachment_type.PNG)
    driver.quit()

@pytest.fixture()
def member_browser(driver):
    email = env["UAT_ACCOUNT"]
    password = env["UAT_PASSWORD"]

    member_page = MemberPage(driver)
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

@pytest.fixture()
def checkout_prime(driver):
    number = env["UAT_TEST_CARD_NUMBER"]
    expiration = env["UAT_TEST_EXPIRATION_DATE"]
    cvc = env["UAT_TEST_CVC_NUMBER"]
    LOGGER.info(f"[Data] checkout paymeny data card nubmer: {number}, expire date: {expiration}, cvc {cvc}")

    prime_page = PrimePage(driver)
    prime_page.load_page("get_prime.html")
    LOGGER.info("[PAGE] Switch to get prime page")
    prime_page.get_prime(number, expiration, cvc)
    
    prime = prime_page.alert_is_present().text
    prime_page.alert_is_present().accept()
    LOGGER.info(f"[Data] prime data: {prime}")

    return prime