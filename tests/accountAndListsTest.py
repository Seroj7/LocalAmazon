import time
import unittest
from pages.accountAndListPage import accountAndList

from selenium import webdriver
from selenium.webdriver.common.by import By

class accountAndListTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.accountAndListObj = accountAndList(self.driver)
        self.driver.get("https://www.amazon.com/ref=nav_logo")

    def test_account_and_lists_element_(self):
        self.accountAndListObj.fill_account_and_list_button()
        time.sleep(20)
#         ?????????????



