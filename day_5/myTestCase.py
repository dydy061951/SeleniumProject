import unittest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()