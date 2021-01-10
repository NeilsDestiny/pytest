from test_PO.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        return

    def goto_department(self):
        pass

    #成员列表
    def get_list(self):
        pass
        # name_webelement_list = self.find_ele(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        # name_list = []
        # for webelement in name_webelement_list:
        #     name_list.append(webelement.text)
        #
        # return name_list