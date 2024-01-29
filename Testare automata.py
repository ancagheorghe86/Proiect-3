import time

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
intram pe elefant.ro
dam click pe parfumuri
dam click pe travel size
dam click pe un produs
'''

chrome = webdriver.Chrome()
chrome.maximize_window()

chrome.get("https://elefant.ro")
time.sleep(2)


chrome.find_element(By.ID, value="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

chrome.find_element(
    by=By.NAME,
    value="SearchTerm"
).send_keys("iphone")

chrome.find_element(
    by=By.NAME,
    value="search"
).click()

# result_elements = chrome.find_elements(
#     by=By.CLASS_NAME, value="product-search-result"
# )
# print(result_elements)

# print(chrome.title)

chrome.find_element(By.XPATH, '//span[contains(@class, "login-prompt js-login-prompt")]').click()

time.sleep(2)

chrome.find_element(By.XPATH, '//a[contains(@class, "my-account-login btn btn-primary btn-block")]').click()

time.sleep(20)
