from selenium import webdriver


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
    def teardown(self):
        self.driver.quit()
        # pass

    def test_hogwards(self):

        print('成功了')