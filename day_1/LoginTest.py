#coding:utf-8
from selenium import webdriver
#打开浏览器
#Chrome后面一定要有括号，代表一个方法动作，去打开
driver=webdriver.Chrome()
#打开登录页面
#get获取一个页面，输入网址，打开此页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#输入用户名
#网页上所有可见的都属于element（元素），比如：链接，按钮，下拉框...
#send_keys：向页面发送键盘上的按键
driver.find_element_by_id("username").send_keys("dydy")
#输入密码
driver.find_element_by_id("password").send_keys("1234567890")
#点击登录按钮
#寻找元素的XPath，可以说是万能定位元素
driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/ul/li[5]/input").click()
