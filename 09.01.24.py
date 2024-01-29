import time

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
intram pe emag.ro
dam click pe parfumuri
dam click pe travel size
dam click pe un produs
'''

chrome = webdriver.Chrome()
chrome.maximize_window()

chrome.get("https://www.emag.ro")
time.sleep(2)


chrome.find_element(By.XPATH, value= '//span[contains(text(),"Bacanie")]').click()

time.sleep(5)

chrome.find_element(By.XPATH, value='//a[contains(text(),"Bacanie")]').click()
time.sleep(10)

chrome.find_element(By.XPATH, value='//a[contains(text(),"Dulceata, Miere")]').click()
time.sleep(10)

time.sleep(20)


