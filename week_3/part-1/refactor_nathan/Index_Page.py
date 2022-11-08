from Action_Utils import *
from selenium.webdriver.common.by import By

class IndexPage(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)

    view_cart_btn_locator = (By.XPATH, "//a[@title = 'View cart']")
    update_item_qty_locator = (By.XPATH, "//input[@title = 'Qty']")
    update_cart_btn_locator = (By.XPATH, "//button[text() = 'Update cart']")
    update_alert_message_locator = (By.CLASS_NAME, "woocommerce-message")
    subtotal_text_locator = (By.XPATH, "//td[@data-title = 'Subtotal']/descendant::bdi")
    checkout_btn_locator = (By.CLASS_NAME, "wc-proceed-to-checkout")

    def get_add_to_cart_btn_locator(self, product_name):
        self.add_to_cart_btn_locator = (By.XPATH, f"//h2[text()='{product_name}']/ancestor::li/a[text()='Add to cart']")

    def click_add_to_cart_btn(self):
        self.find_clickable_elem(self.add_to_cart_btn_locator).click()

    def click_view_cart_btn(self):
        self.find_clickable_elem(self.view_cart_btn_locator).click()

    def get_item_qty_btn(self):
        return self.find_clickable_elem(self.update_item_qty_locator)

    def click_update_cart_btn(self):
        self.find_clickable_elem(self.update_cart_btn_locator).click()

    def is_update_alert_message_present(self):
        self.find_present_elem(self.update_alert_message_locator)

    def get_subtotal_text_locator(self):
        return self.find_present_elem(self.subtotal_text_locator)

    def click_checkout_btn(self):
        self.find_clickable_elem(self.checkout_btn_locator).click()