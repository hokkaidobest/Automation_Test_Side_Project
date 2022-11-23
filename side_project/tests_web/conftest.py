import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def main_broswer():
    options = Options()
    options.chrome_executable_path = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(options = options)
    driver.maximize_window()
    driver.get("http://54.201.140.239/")

    yield driver
    
    driver.quit()