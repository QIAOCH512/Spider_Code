from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from  selenium.webdriver.common.by import By

service = Service(executable_path='./browser_driver/geckodriver.exe')
browser = webdriver.Firefox(service=service)

browser.get("https://pic.netbian.com")
img_list = browser.find_elements(By.XPATH, "//ul[@class='clearfix']/li/a/span/img")

for attr in img_list:
    print(attr.get_attribute('src'))