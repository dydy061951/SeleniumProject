import time

from selenium import webdriver
#1.打开浏览器后台登录页面 进行登录
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
time.sleep(4)
#2.选择商品管理，添加商品
driver.find_element_by_link_text("商品管理").click()
driver.find_element_by_link_text("添加商品").click()
#3.商品分类选择
driver.switch_to.frame("mainFrame")
driver.find_element_by_css_selector("[nullmsg='请输入商品名称！']").send_keys("iphone 4s")
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
driver.find_element_by_id("7").click()
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

#页面太长，点击不了下面的button,怎么操作滚动条
#range是区间，默认从0开始，到长度-1结束，range(10)表示0到9，一共10个数字
time.sleep(3)
ac=ActionChains(driver).send_keys(Keys.TAB)
for a in range(10):
   ac.send_keys(Keys.ARROW_UP)
ac.perform()

# jsgdt="var action=document.documentElement.scrollTop=0"    #js操作滚动条
# driver.execute_script(jsgdt)

#6.上传图片
#6-1点击商品图册
driver.find_element_by_link_text("商品图册").click()
time.sleep(2)
#有些页面控件是javascript在页面加载之后生成的
#implicitily_wait是用来判断整个网页是否加载完毕
#有时页面加载完，但是javascript的控件还没有创建好，所以需要time.sleep()来提高程序的稳定性

#因为真正负责上传文件的页面元素是<input type="file"...
#所以我们可以直接操作这个控件
#这个控件可以直接输入图片文件路径
driver.find_element_by_class_name('webuploader-element-invisible').send_keys("D:/abcd.png")
# jshxgul='var action=document.documentElement.scrollLeft=1000'
# driver.execute_script(jshxgul)
ac1=ActionChains(driver)
for b in range(10):
   ac1.send_keys(Keys.ARROW_RIGHT)
ac1.perform()

#点击开始上传，同时用3个class定位，用css_selector（每个class名称之前加点‘.’）
#放大窗口，否则找不到元素
driver.find_element_by_xpath('//*[@id="uploader"]/div[2]/div[3]/div[2]').click()







