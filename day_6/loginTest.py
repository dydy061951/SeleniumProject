import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day_5.myTestCase import MyTestCase
from day_6.page_object.loginPage import LoginPage
from day_6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    '''
    def test_login(self):
        #1.打开网页
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        #2.输入用户名密码
        from selenium.webdriver.common.by import By
        driver.find_element(By.ID,"username").send_keys("dydy01")
        driver.find_element(By.ID,"password").send_keys("1234567890")
        #3.点击登录按钮
        driver.find_element(By.CLASS_NAME,"login_btn").click()
        #4.验证是否跳转到个人管理中心页面(断言)
        title="我的会员中心 - 道e坊商城 - Powered by Haidao"
        time.sleep(3)
        # assertIn：判断在浏览器的title文字中是否包含我的会员中心这几个字
        self.assertIn("我的会员中心",self.driver.title)
    '''

    def test_login_one(self):
        lp=LoginPage(self.driver)
        lp.open()
        lp.input_username("dydy01")
        lp.input_password("1234567890")
        lp.click_login_button()
        time.sleep(3)
        pcp=PersonalCenterPage(self.driver)
        self.assertEqual(pcp.title,self.driver.title)

