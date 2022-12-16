from page_objects.action_utils import *
from selenium.webdriver.common.by import By

class PrimePage(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)

    get_card_number_iframe_locator = (By.XPATH, "//div[@id = 'card-number']/iframe")
    get_cc_number_input_text_locator = (By.ID, "cc-number")
    get_expiration_date_iframe_locator = (By.XPATH, "//div[@id = 'card-expiration-date']/iframe")
    get_expiration_data_input_text_locator = (By.ID, "cc-exp")
    get_ccv_iframe_locator = (By.XPATH, "//div[@id = 'card-ccv']/iframe")
    get_cvc_valid_input_text_locator = (By.ID, "cc-cvc")
    get_prime_btn_locator = (By.ID, "checkoutBtn")

    def get_prime(self, number, expiration, cvc):
        self.switch_to_iframe(self.find_present_elem(self.get_card_number_iframe_locator))
        self.find_clickable_elem(self.get_cc_number_input_text_locator).send_keys(number)
        self.switch_back_main_page()

        self.switch_to_iframe(self.find_present_elem(self.get_expiration_date_iframe_locator))
        self.find_clickable_elem(self.get_expiration_data_input_text_locator).send_keys(expiration)
        self.switch_back_main_page()

        self.switch_to_iframe(self.find_present_elem(self.get_ccv_iframe_locator))
        self.find_clickable_elem(self.get_cvc_valid_input_text_locator).send_keys(cvc)
        self.switch_back_main_page()

        self.find_clickable_elem((self.get_prime_btn_locator)).click()