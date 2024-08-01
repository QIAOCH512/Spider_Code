from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='./browser_driver/geckodriver.exe')
browser = webdriver.Firefox(service=service)

browser.get("http://www.baidu.com")
browser.find_element(By.ID, 'kw').send_keys('python')

#清空输入框
browser.find_element(By.ID, 'kw').clear()
