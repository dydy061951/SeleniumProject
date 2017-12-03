import os
from selenium import webdriver
from day_5.myTestCase import MyTestCase

#有了 myTestCase 以后，再写测试用例就不需要重新写 setUp 和 tearDown 方法
class ZhuCeTest(MyTestCase):
    """注册模块测试用例"""
    #因为 myTestCase 已经实现了 setUp 和 tearDown 方法，以后再写测试用例久不需要重新实现 setUp 和 tearDown 方法
    def test_zhuce(self):
        """打开注册页面的测试用例"""
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.maximize_window()
        # 获得浏览器中的网址
        #driver.current_url
        # 获取当前浏览器中的标签页的title
        actual=driver.title
        expected="用户注册 - 道e坊商城 - Powered by Haidao"
        self.assertEqual(actual, expected)
        #先获取基本路径
        base_path=os.path.dirname(__file__)
        path=base_path.replace('day_5','report/screen/')
        print(path)
        # get_screenshot_as_file 截取浏览器的图片
        driver.get_screenshot_as_file(path+"zhuce.png")


