from time import sleep

from selenium import webdriver
#1.打开浏览器后台登录页面 进行登录
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
sleep(4)
#2.选择商品管理，添加商品
driver.find_element_by_link_text("商品管理").click()
driver.find_element_by_link_text("添加商品").click()
#有一种特殊的网页，比如左边或者上边有一个导航条，点击导航条会出现一个页面
#开发在一个窗口页面中嵌套多个页面 用iframe框架结构
#其中“商品管理”和“添加商品”属于根节点的网页
#商品名称属于iframe矿机里的被嵌套的子网页
#之前的窗口切换是用于不同网页窗口之间的页面切换，现在情况也是需要网页切换
#switch_to.frame切换窗口到子框架
driver.switch_to.frame("mainFrame")
driver.find_element_by_css_selector("[nullmsg='请输入商品名称！']").send_keys("iphone 4s")
#3.商品分类选择
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
driver.find_element_by_id("7").click()
#javascript定位方法（好使的）
#dqfl='document.getElementsByClassName(" xtishi")[0].childNodes[3].childNodes[1].click()'
#driver.execute_script(dqfl)

#双击最后一项选择分类
#双击是一种特殊的元素操作，它被封装到ActionChains    Action（行为）Chains(链表，类似于数组的东西)这个类中
#java封装到Action这个类中
#double_click():括号里面填入的是定位的页面元素，perform：链表的结束结尾标志，一定要加
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
#4.商品品牌选择 下拉框
sppp=driver.find_element_by_name("brand_id")
Select(sppp).select_by_value("1")
#商品状态 复选框
#driver.find_element_by_name("is_sales").click()  #定位不到
cuxiao='document.getElementsByClassName("web")[0].childNodes[9].childNodes[3].childNodes[1].childNodes[1].click()'
driver.execute_script(cuxiao)
#5.输入关键词 和 描述
driver.find_element_by_name("keyword").send_keys("好用")
driver.find_element_by_name("brief").send_keys("iphone 4s")
#6.提交
driver.find_element_by_class_name("button_search").click()

