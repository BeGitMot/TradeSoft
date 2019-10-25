from .locators import SearchLocators
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchEngine():
    def __init__(self, browser):
        self.browser = browser

    def wait_for_search_results(self, timeout=20):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(SearchLocators.SEARCH_RESULTS))

    def start_search(self, what):
        elem = self.browser.find_element(*SearchLocators.SEARCH_INPUT)
        elem.send_keys(what)
        elem = self.browser.find_element(*SearchLocators.SEARCH_BUTTON)
        elem.click()
