from selenium.webdriver.common.by import By
from test_add_department.page.BasePage import BasePage
from test_add_department.page.ContactPage import ContactPage


class Index(BasePage):
    def goto_contact(self):
        #跳转到通讯录页面
        self.find(By.CSS_SELECTOR,"frame_nav_item_title")
        return ContactPage(self.driver)