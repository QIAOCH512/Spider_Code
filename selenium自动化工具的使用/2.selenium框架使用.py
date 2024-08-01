
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='./browser_driver/geckodriver.exe')
browser = webdriver.Firefox(service=service)

browser.get('http://www.baidu.com')

#让浏览器自动填入我们要搜索的关键字
browser.find_element(By.CSS_SELECTOR, '#kw').send_keys('python')
#让浏览器自动点击搜索按钮
browser.find_element(By.ID, 'su').click()

#获取页面代码
# code = browser.page_source.encode('utf-8')
# print(code.decode())

#获取cookie
# print(browser.get_cookies())

#页面截图
# browser.get_screenshot_as_file('python.png')

#获取当前请求页面的网址
# print(browser.current_url)

#退出浏览器
browser.quit()