from test_PO.page.base_page import BasePage
from test_PO.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    def add_member(self):

        return ContactPage(self.driver)