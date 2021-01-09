from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    def __init__(self,driver:WebDriver=None):
        self._driver=""
        #此处对driver进行复用，如果不存在driver,就构造一个新的
        if driver is None:
            #mian页面需要用，首次使用时构造新driver
            self._driver = webdriver.Chrome()
        else:
            #Login和Register等页面需要用这个方法，避免重复构造driver
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self,by,locator):
        return self._driver.find_element(by,locator)

    def close(self):
        sleep(10)
        self._driver.quit()