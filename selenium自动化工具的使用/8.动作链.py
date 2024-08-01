from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service = Service(executable_path='./browser_driver/geckodriver.exe')
browser = webdriver.Firefox(service=service)

browser.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

iframe = browser.find_element(By.ID, 'iframeResult')
browser.switch_to.frame(iframe)

source = browser.find_element(By.ID, 'draggable')
dest = browser.find_element(By.ID, 'droppable')

#动作链对象
actions = ActionChains(browser)

#移动
actions.drag_and_drop(source, dest)

#执行命令
actions.perform()