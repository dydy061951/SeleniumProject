#encoding=utf-8
from selenium import webdriver

'''
要想学好selenium，最终要的三件事：
1.元素定位：id、name、class、link、
link_text：必须是文本链接，<a>标签，必须得是文本
2.元素操作：click、send_keys
3.javascript
'''
#用javascript实现窗口切换


driver=webdriver.Chrome()
driver.get("http://localhost/")

#javascript和python是不同的语言，pycharm是用来写python语言的
#想要在python执行javascript语言
js='document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)#通过浏览器执行脚本（执行上段这个js的脚本）去定位到这个元素
#先要在点击 登录 之前删除连接中的target属性，这样新窗口就会在当前页面打开了
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("dydy01")
driver.find_element_by_id("password").send_keys("1234567890")
driver.find_element_by_class_name("login_btn").click()
