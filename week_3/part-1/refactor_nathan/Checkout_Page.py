from Action_Utils import *
from selenium.webdriver.common.by import By

class CheckoutPage(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)

    create_account_btn_locator =  (By.ID, "createaccount")
    place_order_btn_locator = (By.ID, "place_order")
    checkout_alert_message_locator = (By.XPATH, '//ul[@class = "woocommerce-error"]')

    def get_ckeckout_form_column_locator(self, column):
        self.ckeckout_form_column_locator = (By.ID, column)

    def fill_in_ckeckout_form_column(self, value):
        self.find_clickable_elem(self.ckeckout_form_column_locator).send_keys(value)

    def click_create_account_btn(self):
        self.find_clickable_elem(self.create_account_btn_locator).click()

    def click_place_order_btn(self):
        self.find_clickable_elem(self.place_order_btn_locator).click()

    def get_checkout_alert_message(self):
        return self.find_present_elem(self.checkout_alert_message_locator)