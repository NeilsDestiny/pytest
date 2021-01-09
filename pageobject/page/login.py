from selenium.webdriver.common.by import By
from pageobject.page.base_pase import BasePage
from pageobject.page.register import Register

class Login(BasePage):
    # 扫描二维码
    def scan(self):
        pass

    # 进入注册页面
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)
