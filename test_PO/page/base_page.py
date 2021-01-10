import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        # 此处对driver进行复用，如果不存在driver,就构造一个新的
        if driver is None:
            # main页面需要用，首次使用时构造新driver
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            # Login和Register等页面需要用这个方法，避免重复构造driver
            self.driver = driver
        self.driver.implicitly_wait(3)

    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()
        # 打开cookie文件
        with open(r"D:\Python\pytest/\test_PO\page\cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find_ele(self, by, value):
        return self.driver.find_element(by,value)

    def close(self):
        sleep(10)
        self.driver.quit()

