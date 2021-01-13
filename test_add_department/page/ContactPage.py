from time import sleep
from selenium.webdriver.common.by import By
from test_add_department.page.AddDepartmentPage import AddDepartment
from test_add_department.page.BasePage import BasePage

class ContactPage(BasePage):
    def goto_add_department(self):
        self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        sleep(3)
        self.find(By.CSS_SELECTOR,".js_create_party").click()
        return AddDepartment(self.driver)

    def get_department_list(self):
        _department = self.find(By.XPATH,'//ul[@role="group" and @class="jstree-children"]//li')
        department_list = []
        for department in _department:
            department_list.append(department.text)

        return department_list