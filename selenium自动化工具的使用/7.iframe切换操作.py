from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='./browser_driver/geckodriver.exe')
browser = webdriver.Firefox(service=service)

browser.get("http://douban.com")
login_iframe = browser.find_element(By.XPATH, "//div[@class='login']/iframe")

#切换到子页面
browser.switch_to.frame(login_iframe)

browser.find_element(By.CLASS_NAME, "account-tab-account").click()
browser.find_element(By.ID, "username").send_keys("QIAO")