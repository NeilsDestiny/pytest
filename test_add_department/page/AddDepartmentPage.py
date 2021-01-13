from time import sleep
from selenium.webdriver.common.by import By
from test_add_department.page.BasePage import BasePage
from test_add_department.page.ContactPage import ContactPage

class AddDepartment(BasePage):
    def add_department(self,department):
        self.find(By.CSS_SELECTOR,".ww_inputText").send_keys(department)
        #点击下拉框
        self.find(By.CSS_SELECTOR,"js_toggle_party_list").click()
        sleep(3)
        self.find(By.ID,".1688850760940284_anchor").click()
        sleep(2)
        #确定按钮
        self.find(By.CSS_SELECTOR,".ww_btn_Blue").click()
        return ContactPage(self.driver)

    def btn_cancel(self):
        self.find(By.CSS_SELECTOR,"qui_btn ww_btn").click()
        return ContactPage(self.driver)