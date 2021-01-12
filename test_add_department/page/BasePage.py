from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver=driver

        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")
        #手动登录
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        sleep(5)


    def teardown(self):
        self.driver.quit()

