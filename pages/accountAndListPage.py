from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class accountAndList():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.action = ActionChains(driver)


    def fill_account_and_list_button(self):
        accountAndListElement = self.driver.find_element(By.ID, "nav-link-accountList")
        ActionChains(self.driver).move_to_element(accountAndListElement).perform()
        # self.action.move_to_element(accountAndListElement)
        # self.action.perform()






