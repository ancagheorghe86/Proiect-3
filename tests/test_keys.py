import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestKeys(unittest.TestCase):
    URL = "https://the-internet.herokuapp.com/login"
    def setUp(self) -> None:  # use type annotations
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_keys(self):
        username_input = self.driver.find_element(By.ID, "username")
        username_input.send_keys("tomsmith")

        time.sleep(5)

        username_input.send_keys(Keys.CONTROL, 'A')
        username_input.send_keys(Keys.DELETE)

        time.sleep(5)

        username_password = self.driver.find_element(By.ID, "password")
        username_password.send_keys("SuperSecretPassword!")

        self.driver.find_element(By.CSS_SELECTOR, ".radius").click()
        time.sleep(5)