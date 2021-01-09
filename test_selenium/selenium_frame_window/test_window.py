#多窗口处理
from time import sleep
from selenium.webdriver.common.by import By
from test_selenium.selenium_frame_window.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)
        #获取全部的窗口
        windows = self.driver.window_handles
        print(windows)
        #切换到最后一个窗口
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys("username")
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('17712345678')
        # print(self.driver.current_window_handle)
        sleep(1)
        #关闭当前窗口
        # self.driver.close()
        # print(self.driver.current_window_handle)
        #切换到第一个窗口
        self.driver.switch_to_window(windows[0])
        # print(self.driver.current_window_handle)
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('login_username')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('login_password')
        sleep(1)
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()
        sleep(3)