import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



#禁止加载图片
prefs = {'profile.managed_default_content_settings.images': 2}
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', prefs)
service = Service(executable_path='./browser_driver/chromedriver_win64.exe')

#无头模式
# options.add_argument('-headless')

#请求头设置
# user_agent = '12345'
# options.add_argument(f'user-agent={user_agent}')

#去除开发者警告
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option('excludeSwitches', ['enable-automation'])

#代理设置
# options.add_argument("--proxy-service=")


browser = webdriver.Chrome(service=service, options=options)

#设置浏览器窗口大小
browser.set_window_size(1000,1000)

#执行JS代码
browser.execute_script('window.open("http://www.bing.com")')

browser.get('http://www.baidu.com')

time.sleep(10)
browser.quit()
