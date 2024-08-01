
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='./browser_driver/geckodriver.exe')
browser = webdriver.Firefox(service=service)

browser.get("http://www.baidu.com")

#选中一个元素
search_input = browser.find_element(By.NAME, 'wd')
#在输入框中输入
search_input.send_keys('python')
#完成回车操作
search_input.send_keys(Keys.ENTER)