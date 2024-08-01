from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service= Service(executable_path='./browser_driver/geckodriver.exe')
browser = webdriver.Firefox(service=service)

browser.get('https://www.icswb.com/')

li_list = browser.find_elements(By.CSS_SELECTOR, '#NewsListContainer li')
print(li_list)