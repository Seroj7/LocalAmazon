from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SearchBox():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def fill_search_field(self, search):
        searchFieldElement = self.driver.find_element(By.ID, "twotabsearchtextbox")
        searchFieldElement.send_keys(search)

    def click_to_search_button(self):
        searchButtonElement = self.driver.find_element(By.ID, "nav-search-submit-button" )
        searchButtonElement.click()


