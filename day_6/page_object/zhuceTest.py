import  unittest

import time

from day_5.myTestCase import MyTestCase
from day_6.data_base.connectDB import connDb


class ZhuCeTest(MyTestCase):
    def test_zhuce(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("dydy04")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("userpassword2").send_keys("123456")
        driver.find_element_by_name("mobile_phone").send_keys("13112030002")
        driver.find_element_by_name("email").send_keys("1234567@qq.com")
        driver.find_element_by_class_name("reg_btn").click()
        time.sleep(3)
        #断言：验证检查数据库的最新一条用户名记录是否是刚新增注册的用户名一致
        selfusername="dydy04"
        actual=connDb()[1]
        self.assertEqual(selfusername,actual)
        print(connDb()[1])
