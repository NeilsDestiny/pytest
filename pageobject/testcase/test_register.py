from pageobject.page.main import Main

class TestRegister():
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()

    def test_login_to_register(self):
        assert self.main.goto_login().goto_register().register()

    # 关闭driver
    def teardown(self):
        self.main.close()
