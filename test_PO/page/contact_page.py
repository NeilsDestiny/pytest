from selenium.webdriver.common.by import By

from test_PO.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        return

    def goto_department(self):
        pass

    #通信录成员列表
    def get_list(self):
        # return Ture
        #返回通讯录里的人员信息
        name_webelement_list = self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        print(name_webelement_list)
        name_list = []
        for webelement in name_webelement_list:
            name_list.append(webelement.text)

        return name_list