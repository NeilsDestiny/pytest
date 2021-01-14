import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self.driver=driver
        self.driver.implicitly_wait(5)
        # self.driver.get("https://work.weixin.qq.com/")
        # self.driver.maximize_window()
        # #手动登录
        # self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        # sleep(5)

    #通过cookic登录
    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()
        # 打开cookie文件
        with open(r"D:\Python\pytest/\test_add_department\page\cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def quit(self):
        self.driver.quit()

    def find(self,by,value):
        return self.driver.find_element(by,value)

