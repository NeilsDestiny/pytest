from time import sleep
from selenium.webdriver.common.by import By
from test_add_department.page.BasePage import BasePage
from test_add_department.page.ContactPage import ContactPage


class AddDepartment(BasePage):
    def add_department(self,department):
        self.find(By.CSS_SELECTOR,".form div:nth-child(1) input").send_keys(department)
        #点击下拉框
        self.find(By.CSS_SELECTOR,".js_parent_party_name").click()
        sleep(1)
        self.find(By.XPATH,'//form[@class="form"]//a[@tabindex="-1" and @id="1688850760940284_anchor"]').click()
        sleep(1)
        #确定按钮
        self.find(By.CSS_SELECTOR,".qui_dialog_foot a:nth-child(1)").click()
        return ContactPage(self.driver)

    def btn_cancel(self):
        self.find(By.CSS_SELECTOR,".qui_dialog_foot a:nth-child(2)").click()
        return ContactPage(self.driver)