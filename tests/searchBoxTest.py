import time
import unittest

from selenium import webdriver
from pages.searchBoxPage import SearchBox

class SearchBoxTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.searchBoxObj = SearchBox(self.driver)
        self.driver.get('https://www.amazon.com/ref=nav_logo')

    def test_search_box(self):
        self.searchBoxObj.fill_search_field("AGV helmet")
        self.searchBoxObj.click_to_search_button()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()