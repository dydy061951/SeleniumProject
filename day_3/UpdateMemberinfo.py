from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

'''
修改个人信息
1.登录系统
2.进入账号设置，点击个人资料
3.修改个人信息
'''

#1.登录系统
driver=webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("dydy01")
#driver.find_element_by_id("password").send_keys("1234567890")
#输入完用户名后，在敲回车进入主界面，利用键盘Tab键来切换到密码输入框，Keys代表键盘上所有的按键
#也可在输入完用户名后直接在后面切换TAB键，是针对用户名元素下的切换
#driver.find_element_by_id("username").send_keys("dydy01").send_keys(Keys.TAB)
#此方法是针对在整个浏览器界面上的TAB切换
#Chains链表和数组不同，数组有固定的长度，链表必须有明确的结束标志：perform()，结尾
ActionChains(driver).send_keys(Keys.TAB).send_keys("1234567890").send_keys(Keys.ENTER).perform()
sleep(3)

#2.点击进入账号设置，点击个人资料
driver.find_element_by_link_text("账号设置").click()
#a标签链接嵌套多个文本，要定位文字最好用部分文本链接较准确
driver.find_element_by_partial_link_text("个人资料").click()

#3.修改个人信息
#3-1：修改真实姓名
#clear是清空的意思，用来清空元素中原本的内容，最好在每次执行sendkeys时都执行一边clear操作来清空
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("大马猴")

#3-2性别选择（radio类型单选）,如果界面上出现两个value值为2的元素，那么可以利用属性组合来定位唯一，id与value组合即为唯一
#css可以用多个属性组合定位一个元素，一个元素的多个属性之间不能有空格
driver.find_element_by_css_selector("#xb[value='2']").click()

#3-3日期控件选择
jsdate='document.getElementById("date").removeAttribute("readonly")'
driver.execute_script(jsdate)
#用arguments改写上面的输入，用selenium的定位方式来找到这个元素之后，再对元素执行javascript脚本的删除只读readonly操作；会比javascript来定位到这个元素更快捷一些
#date=driver.find_element_by_id("date")
#driver.execute_script("arguments[0].removeAttribute('readonly')",date)

driver.find_element_by_id("date").clear()
#也可以用javascript jquery方法来改变value的日期值（自己总结方法，好用）
#jsdate1='$(document.getElementById("date")).attr("value","2017-11-25")'
#driver.execute_script(jsdate1)
driver.find_element_by_id("date").send_keys("2017-11-25")
#用selenium调用javascript一共有两个关键字：
#1.arguments[0]：表示用python语言代替一部分javascript
#好处是，有时，selenium定位比较容易
#2.return 把javascript的执行结果返回给python语言
#好处是，有时，selenium定位不到的元素，我们可以用javascript定位到；常用在元素很难定位或定位不到时运用
#date1=driver.execute_script("return document.getElementById('date')")
#这句话==date=driver.find_element_by_id("date")
#date1.click()   #点开日期控件

#3-4输入QQ号
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("77589914")

#4.确认提交信息
driver.find_element_by_class_name("btn4").click()
sleep(2)
#5.弹窗提示点击确定
#alert右键检查不了html代码的弹出框，叫做alert，有单独的方法来处理
#alert控件不是html代码生成的，所以implicitly_wait隐式等待对这个控件不管用
#切换到alert的方法，和切换窗口的方法类似
#alert：弹出框；accept：接受，同意，确定；dismiss：拒绝，取消（也适用于窗口右上角的x关闭图标）
driver.switch_to.alert.accept()


