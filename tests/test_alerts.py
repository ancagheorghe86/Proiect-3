import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAlerts(unittest.TestCase):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    def setUp(self) -> None:  # use type annotations
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def tearDown(self) -> None:
        self.driver.quit()
    def test_simple_alert(self):
        # 1. click pe buton
        # 2. interactioneaza cu alerta click/camcel
        # 3. verifica rezultat afisat "you succesfully clicked on alert, etc"
        self.driver.find_element(By.CSS_SELECTOR, "[onclick='jsAlert()']").click()

        time.sleep(4)

        expected_result = "You succesfully clicked an alert"
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, expected_result)
        time.sleep(4)

    def test_confirm_alert(self):
        # 1. click pe buton
        self.driver.find_element(By.CSS_SELECTOR, "[onclick='jsConfirm()']").click()
        time.sleep(4)


        # interactioneaza cu alerta dand click/cancel
        alerta = self.driver.switch_to.alert
        alerta.accept()

        expected_result = "You clicked: Ok" # de obicei este luat din REQUIREMENTS
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, expected_result)
        time.sleep(1)

    def test_accept_prompt_with_text(self):
        # 1. click pe buton
        self.driver.find_element(By.CSS_SELECTOR, "[onclick='jsPrompt()']").click()
        time.sleep(4)

        # interactioneaza cu alerta dand click/cancel
        alerta = self.driver.switch_to.alert

        text = "blabla"
        alerta.send_keys(text) #scrie in prompt textul dat
        time.sleep(2)
        alerta.accept()


        expected_result = f"You entered: {text}"  # de obicei este luat din REQUIREMENTS
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, expected_result)
        time.sleep(1)


