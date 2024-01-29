from driver import
from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    URL = "https://demo.nopcommerce.com/login"
    INPUT_EMAIL = (By.ID, "Email") # acel locator,  tuplu ce va fi dat ca parametru functiei find din BasePage
    INPUT_PASS = (By.ID, "Password")
    BUTON_LOGIN = (By.CLASS_NAME, "login-button")

    def open(self):
        self.driver.get(self.URL)
    def set_email(self, email):
        self.type(self.INPUT_EMAIL, email)

    def set_password(self, password):
        self.type(self.INPUT_PASS, password)

    def click_login_button(self):
        self.button_click(self.BUTON_LOGIN)

