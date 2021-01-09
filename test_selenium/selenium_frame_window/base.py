import os
from selenium import webdriver

class Base():
    def setup(self):
        #使用os模块的getenv方法来获取声明环境变量browser
        browser = os.getenv("browser")
        #判断browser的值
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        #隐式等待
        self.driver.implicitly_wait(5)
        #最大化窗口
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
        # pass
