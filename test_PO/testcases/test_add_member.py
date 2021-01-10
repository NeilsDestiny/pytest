from test_PO.page.main_page import MainPage

class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.close()

    def test_add_member(self):
        #1.首页跳转到添加成员 2.添加成员 3.获取成员信息
        result = self.main.goto_add_member().add_member().get_list()
        assert result == True