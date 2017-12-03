#encoding=utf-8
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://localhost/")

driver.find_element_by_link_text("登录").click()

#从浏览器中的所有窗口中，排除第一个窗口，剩下第二个窗口
#把selenium切换到第二个窗口
firstWindow=driver.current_window_handle
totalWindows=driver.window_handles
for i in totalWindows:
    if i==firstWindow:
        driver.close()
    else:
        driver.switch_to.window(i)

driver.find_element_by_id("username").send_keys("dydy")
driver.find_element_by_id("password").send_keys("1234567890")
driver.find_element_by_class_name("login_btn").click()