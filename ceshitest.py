from selenium import webdriver


#Chrome正收到自动测试软件的控制 去掉的方法
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)

driver.get("http://localhost/index.php?m=user&c=public&a=login")