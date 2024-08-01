import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#1.使用Service将浏览器驱动程序导入到selenium框架内部
service = Service(executable_path='browser_driver/chromedriver_win64.exe')

#2.创建浏览器对象
browser = webdriver.Chrome(service=service)

#3.访问百度网站
browser.get('http://www.baidu.com')

#4.代码休眠
time.sleep(5)

#5.使用selenium自带的方法退出浏览器
browser.quit()
