import unittest
from selenium import webdriver
import time

class MemberManageTest(unittest.TestCase):
    #变量前面加上 self. 表示整个变量是类的属性，可以被所有的方法调用访问
    def setUp(self):
        # 打开浏览器
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)#设置隐式等待
        # driver.maximize_window()#窗口最大化

    def tearDown(self):
        # quit():退出整个浏览器
        # close(): 关闭一个浏览器标签
        # 代码编写和调试的时候，需要在quit()方法前加一个时间等待
        time.sleep(60)
        self.driver.quit()

    def  test_add_member(self):   #添加会员
        driver=self.driver   #将属性变为一个局部变量
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        #登录后台系统
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").click()
        time.sleep(3)
        #会员管理
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("dydy03")
        driver.find_element_by_name("mobile_phone").send_keys("13111260004")
        driver.find_element_by_css_selector("[name='sex'][value='1']").click()
        driver.find_element_by_id("birthday").send_keys("2017-11-26")
        driver.find_element_by_name("email").send_keys("4456789@qq.com")
        driver.find_element_by_name("qq").send_keys("224598702")