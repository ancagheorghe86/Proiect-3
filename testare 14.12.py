# import time
#
#
# def test_form_email():
#     pass
#
# def test_form_incorect_email_password():
#     pass
#
# def test_form_correct_email_password():
#     pass
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

url = "https://formy-proiect.herokuapp.com/form"

chrome = webdriver.Chrome()
chrome.get(url)
chrome.maximize_window()
time.sleep(2)


input_first_name = chrome.find_element(By.ID, "first-name")
input_last_name = chrome.find_element(By.ID, "last-name")
input_job_title = chrome.find_element(By.ID, "job-title")

input_first_name.send_keys("Mihai")
input_last_name.send_keys("Popescu")
input_job_title.send_keys("Automation tester")

radio_college = chrome.find_element(By.XPATH, "//*[@id='radio-button-2']")
radio_college.click()

male_check = chrome.find_element(By.ID, "checkbox-1")
male_check.click()

time.sleep(1)

submit_button = chrome.find_element(By.CLASS_NAME, "btn-primary")
submit_button.click()

succes_message = chrome.find_element(By.CLASS_NAME, "alert-succes")

print(succes_message.text)

assert succes_message.is_displayed()


time.sleep(10)