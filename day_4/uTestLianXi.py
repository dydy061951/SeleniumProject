from selenium import webdriver
import ddt
import time

from day_4.readCsv2 import read


@ddt.ddt
class UTestLianXi:
    member_info = read("member_info.csv")

    def login(self,driver):
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").click()
        time.sleep(3)

    @ddt.data(*member_info)
    def addmember(self,driver,row):
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector("[name='sex'][value='" + row[2] + "']").click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        time.sleep(3)
        driver.switch_to.default_content()

if __name__ == '__main__':
    driver=webdriver.Chrome()
    b=driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
    UTestLianXi().login(driver)
    UTestLianXi().addmember(driver)
    time.sleep(20)
    driver.quit()