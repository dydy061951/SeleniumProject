import unittest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class DengluTest(unittest.TestCase):
    #三个双引号，表示文档字符串，也是一种注释，和#号注释的区别是：三个双引号注释会显示在文档中
    """登录模块测试用例"""
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

    def test_denglu(self):
        """登录测试正常情况测试用例"""
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_name("username").send_keys("dydy01")
        driver.find_element_by_name("password").send_keys("1234567890")
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        print("当前用户名：dydy01")