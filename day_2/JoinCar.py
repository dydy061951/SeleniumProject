#encoding=utf-8
from time import sleep, time
from selenium import webdriver
#firefox浏览器45以下版本都不需要驱动文件，46开始以上版本需要驱动文件
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://localhost/")
#隐式等待，一经设置，对后面的所有语句都有效果，所以在创建浏览器时设置一次就可以了
#implicitly 含蓄的、委婉的意思
driver.implicitly_wait(30)
#窗口最大话

#进入登录页面

#在点击登录按钮之前，我们需要先删除target属性
#但是javascript定位方式比selenium麻烦
#可不可以用selenium的定位方式来替换javascript的定位方式呢
#用arguments关键字，可以把元素定位作为一个参数，替换到javascript语句中
login_link=driver.find_element_by_link_text("登录")
#在execute_script方法中有两个参数，arguments[0]中的0下标代表所在的参数语句当中后的一个参数，即为login_link
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()

#登录用户名密码
driver.find_element_by_id("username").send_keys("dydy01")
driver.find_element_by_id("password").send_keys("1234567890")
driver.find_element_by_id("password").submit()
#submit()用于提交form表单，form是html中的一个元素
#form表单的任何子孙节点都可以调用submit（）方法提交表单
#不推荐使用，因只有form表单可以使用，再它不属于一种模拟人工操作行为，而是填写完信息系统自动向上提交表单的一种行为

#time.sleep(4)
#time.sleep到底设置几秒，应该使用隐式等待，会自动判断网页是否加载完毕，当加载完毕立刻开始执行后续的操作
#我们需要设置一个最大时间，不能让程序无限等待，一般时间是30秒

#进入商城购物病搜索iphone产品
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()

js='document.getElementsByClassName("shop_01-imgbox")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)
#因为我们copy的是selector，所以要用css_selector的方式定位
#iphone_img="body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
iphone_link='div.protect_con > div > div.shop_01-imgbox > a'
#img是标签名，>标签前面的是父节点，后面的是子节点
#如果想在css中写class属性，那么前面要加上小数点
#：nth-child（2），表示当前节点在家中排行老二，是它父亲的第二个儿子
driver.find_element_by_css_selector(iphone_link).click()
#为什么要把css selector中的内容改的越短越好？
#因为涉及到越多的节点，那么代码的健壮性和可维护性就越差
#因为开发一旦修改页面时，修改了这些节点，那么元素就会定位失败

sleep(5)
#加入购物车
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
driver.find_element_by_class_name("add-address").click()

#添加地址
driver.find_element_by_name("address[address_name]").send_keys("Jack")
driver.find_element_by_name("address[mobile]").send_keys("13111180002")
#选择下拉框
#方法一：
'''
driver.find_element_by_css_selector("[value='110000']").click()
driver.find_element_by_css_selector("[value='110000']").click()
driver.find_element_by_css_selector("[value='110101']").click()
'''

#方法二：
#下拉框是一种比较特殊的网页元素，selenium专门为下拉框提供了一种定位方式
#需要把这个元素从WebElement类型转换成Select类型
sheng=driver.find_element_by_id("add-new-area-select")   #select父节点，返回值是一个element元素类型
#Select是selenium专门创建的一个类，用于操作下拉框使用的
#Select这个类中封装了很多操作下拉框的方法
Select(sheng).select_by_value("230000")
#shi=driver.find_element_by_id("linkagesel_013712")    #id为动态元素值，无法具体定位
#Select(shi).select_by_value("230100")
#qu=driver.find_element_by_id("linkagesel_816249")
#Select(qu).select_by_value("230103")

#利用标签名来检索
#弹窗页面查看共有3个select下拉标签，利用下标值来进行具体定位
shi=driver.find_elements_by_tag_name("select")[1]
#利用下标值来定位select下的option的值
Select(shi).select_by_index(2)
qu=driver.find_elements_by_tag_name("select")[2]
#根据文本来查找元素
Select(qu).select_by_visible_text("建华区")   #deselect不选择哪个值

driver.find_element_by_name("address[address]").send_keys("北京市昌平区")
driver.find_element_by_name("address[zipcode]").send_keys("100000")
driver.find_element_by_class_name("aui_state_highlight").click()
