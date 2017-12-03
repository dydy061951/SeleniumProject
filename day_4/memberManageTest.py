import unittest
#1.导入 ddt 代码库，此代码库只适用于unittest框架中
import ddt
from selenium import webdriver
import time

from day_4.readCsv2 import read

#2.装饰这个类，明确ddt下的ddt这个方法
@ddt.ddt
class MemberManagerTest(unittest.TestCase):
    #3.调用之前写好的 read()方法，获取配置文件中的数据
    member_info = read("member_info.csv")

    #此注释表示，在当前类，下面的setUpClass方法只执行一次
    @classmethod
    def setUpClass(cls):  #在个方法是在所有方法执行之前只执行一次
        print("在所有方法之前，只执行一次")
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls): #表示在所有方法之后只执行一次
        print("在所有方法结束后，只执行一次")
        time.sleep(12)
        cls.driver.quit()

    def test_a_login(self):
        print("登录系统")
        driver=self.driver
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").click()
        time.sleep(3)

    #python中集合或列表前的 * 表示，把集合中的元素拆开，一个一个写
    #5. @ddt.data()测试数据来源于 read()方法
    #把数据表中的每一行传入方法，在方法中增加一个参数row
    @ddt.data(*member_info)   #ddt方法从 上面的member_info中读取数据
    def test_b_addmember(self,row):
        print("添加会员")
        driver=self.driver
        #每组测试数据就是一条测试用例，每条测试用例应该是独立的，不能因为上一条测试用例失败而导致后面的用例不能被正常执行，所以不推荐用for循环
        #应该用 ddt 装饰器，去修饰这个方法，达到测试用例每条都可独立执行的目的
        # ddt 是 数据驱动测试 data driver test
        #4.注释掉 for 循环,改变代码中所有的缩进
        # for row in read("member_info.csv"):
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        #print(type(row[2]))
        #"[value={0}]".format(row[2])   {}大括号内为可变变量，format：格式化
        #"[value={0}]".format(row[2])   {0}大括号内的数字是 format的0个下标元素开始被格式化传入到value值中
        # driver.find_element_by_css_selector("[value={0}]".format(row[2])).click()
        driver.find_element_by_css_selector("[name='sex'][value='"+row[2]+"']").click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        time.sleep(3)


        #之前的代码是能够自动运行，但是还不能自动判断程序运行的是否正确
        #自动化代码，不能找人总是看着运行，检查是否执行正确
        # actual 实际结果，从执行测试用例后，页面上实际显示的结果
        actual_username=driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text       #定位元素，  .text 获取这个元素上的文本
        # # expected 期望结果，相当于手工测试用例或是需求文档、一般来自于配置文件上的预期结果
        expected_username=row[0]

        # 断言和 if...else 语句类似，是用来做判断的
        # if actual_username==expected_username:
        #     print("测试通过")
        # else:
        #     print("测试失败")

    #断言叫 assert，断言是框架提供的，想要调用断言，那么必须加上 self，因为测试用例类继承了框架中的 TestCase 类，也继承了这个类中的断言，所以我们可以直接用断言方法

   # 断言有几个特点：
   #  1.断言比较简洁
   #  2.断言只关注错误的测试用例，只有断言出错的时候才会打印信息，正确时是没有任何提示的
   #  3.断言报错时，后面的代码将不会继续执行.前面的步骤失败了，后面的步骤久不需要继续尝试了，浪费性能

        # 切换到父框架
        driver.switch_to.default_content()

        self.assertEqual(actual_username, expected_username)

if __name__ == '__main__':
    unittest.main()
