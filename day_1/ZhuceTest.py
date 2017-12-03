#encoding=utf-8
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_link_text("注册").click()
#窗口切换：把selenium去切换到新的窗口工作
#浏览器当前窗口的句柄，current_window_handle是一个属性
firstWindow=driver.current_window_handle   #cwh代表的是浏览器当中的第一个窗口
print(firstWindow)   #输出为一段加密字符串
#selenium只提供了selenium工作窗口的名字，并没有提供第二个窗口的名字，如获得新开启的第二个新窗口，我们得自己求
totalWindows=driver.window_handles   #浏览器中的所有窗口句柄   获取到的是一个数组
#循环数组，如果当前窗口
for item in totalWindows:
    if item==firstWindow:
        driver.close()
    else:
        driver.switch_to.window(item)    #switch_to窗口切换到下一迭代窗口，为新开启的第二个新窗口

driver.find_element_by_name("username").send_keys("dydy02")
driver.find_element_by_name("password").send_keys("1234567890")
driver.find_element_by_name("userpassword2").send_keys("1234567890")
driver.find_element_by_name("mobile_phone").send_keys("13111180003")
driver.find_element_by_name("email").send_keys("568978778@qq.com")
#driver.find_element_by_xpath("//input[@value='注册']").click()   #方法同样可行
driver.find_element_by_class_name("reg_btn").click()


