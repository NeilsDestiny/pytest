from time import sleep
from selenium.webdriver.common.by import By
from test_add_department.page.BasePage import BasePage

class ContactPage(BasePage):
    def goto_add_department(self):
        #点击通讯录
        self.find(By.CSS_SELECTOR,'.frame_nav a:nth-child(2)').click()
        #点击“+”
        self.find(By.CSS_SELECTOR,'.member_colLeft_top_addBtn').click()
        sleep(1)
        #点击添加部门
        self.find(By.CSS_SELECTOR,".js_create_party").click()
        from test_add_department.page.AddDepartmentPage import AddDepartment
        return AddDepartment(self.driver)


    def get_department_list(self):
        _department = self.driver.find_elements(By.XPATH,'//ul[@role="group" and @class="jstree-children"]//li')
        department_list = []
        for department in _department:
           department_list.append(department.text.strip())

        return department_list