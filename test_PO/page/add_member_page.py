from selenium.webdriver.common.by import By

from test_PO.page.base_page import BasePage
from test_PO.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    def add_member(self):
        #添加用户，输入成员信息
        self.find_ele(By.ID,"username").send_keys("皮城女警")
        self.find_ele(By.ID,"memberAdd_acctid").send_keys("1234567")
        self.find_ele(By.ID,"memberAdd_phone").send_keys("13687293712")
        self.find_ele(By.CSS_SELECTOR,".js_btn_save").click()

        #跳转到通讯录
        return ContactPage(self.driver)