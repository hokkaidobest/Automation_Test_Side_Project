from page_objects.action_utils import *
from selenium.webdriver.common.by import By

class MemberPage(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)

    get_email_input_text_locator = (By.ID, "email")
    get_password_input_text_locator = (By.ID, "pw")
    get_log_in_btn_locator = (By.XPATH, "//button[@class = 'login100-form-btn']")
    get_log_out_btn_locator = (By.XPATH, "//div[@class = 'profile__content']/button")

    def click_profile_btn(self):
        self.find_clickable_elem((By.CSS_SELECTOR, f'a[href="./profile.html"]')).click()

    def log_in(self, email, password):
        self.find_clickable_elem((self.get_email_input_text_locator)).send_keys(email)
        self.find_clickable_elem((self.get_password_input_text_locator)).send_keys(password)
        self.find_clickable_elem((self.get_log_in_btn_locator)).click()

    def get_user_jwt_token(self):
        token = self.driver.execute_script("return localStorage.getItem('jwtToken')")

        return token

    def log_out(self):
        self.find_clickable_elem((self.get_log_out_btn_locator)).click()

    def set_user_jwt_token(self, token):
        self.driver.execute_script(f"localStorage.setItem('jwtToken', '{token}')")