from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    account_created_heading_xpath = "//div[@id='content']/h1"

    def display_status_of_account_created_heading(self, expected_heading):
        return self.driver.find_element(By.XPATH, self.account_created_heading_xpath).text.__eq__(expected_heading)