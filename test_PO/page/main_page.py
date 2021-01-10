from selenium.webdriver.common.by import By

from test_PO.page.add_member_page import AddMemberPage
from test_PO.page.base_page import BasePage


class MainPage(BasePage):
    def goto_contact(self):
        pass

    def goto_add_member(self):
        self.find_ele(By.CSS_SELECTOR,".index_service_cnt_item_title").click()
        return AddMemberPage(self.driver)

