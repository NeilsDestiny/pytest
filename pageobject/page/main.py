from selenium.webdriver.common.by import By
from pageobject.page.base_pase import BasePage
from pageobject.page.login import Login
from pageobject.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"
    def goto_register(self):
        #点击立即注册按钮
        self.find(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)

    def goto_login(self):
        #点击登录按钮
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return Login(self._driver)
