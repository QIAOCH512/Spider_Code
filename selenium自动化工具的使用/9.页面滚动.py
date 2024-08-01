import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


service = Service(executable_path='./browser_driver/geckodriver.exe')
browser = webdriver.Firefox(service=service)

browser.get("http://36kr.com")


#绝对位置
# for num in range(1, 10):
#     browser.execute_script(f'window.scrollTo(0, {num * 700})')
#     time.sleep(1)


#相对位置
for num in range(1, 10):
    browser.execute_script(f'window.scrollBy(0, {num * 700})')
    time.sleep(1)