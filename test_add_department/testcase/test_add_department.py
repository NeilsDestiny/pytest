from test_add_department.page.Index import Index

class TestAddDepartment:
    def setup_class(self):
        self.index = Index()

    def teardown(self):
        self.index.quit()

    def test_add_department(self):
        res = self.index.goto_contact().goto_add_department().add_department("test2").get_department_list()
        assert "test1" in res