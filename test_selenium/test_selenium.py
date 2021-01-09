import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDefaultSuite:
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_cookie(self):
        # #获取cookies
        # cookies = self.driver.get_cookies()
        # #保存cookie到文件中
        # with open("cookie.json","w") as f:
        #   #存储cookie到cookie.json
        #   json.dump(cookies,f)

        self.driver.get("https://work.weixin.qq.com/")
        # self.driver.maximize_window()
        # 打开cookie文件
        with open("cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        # 企业微信的点击客户联系
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]/span').click()

    @pytest.mark.skip
    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        # self.driver.maximize_window()
        sleep(3)
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("测试")
        self.driver.find_element(By.ID, "su").click()
        sleep(5)
        self.driver.close()
