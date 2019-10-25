from .locators import BasePageLocators
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def scroll_to_elem(self, elem):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", elem)

    def open_login_form(self):
        link = self.browser.find_elements(*BasePageLocators.LOGIN_BUTTON)
        link[1].click()
        #link.send_keys(webdriver.common.keys.Keys.SPACE)

    def login(self, name, password):
        elem = self.browser.find_element(*BasePageLocators.LOGIN_NAME)
        elem.send_keys(name)

        elem = self.browser.find_element(*BasePageLocators.LOGIN_PASSWORD)
        elem.send_keys(password)

        button_submit = self.browser.find_element(*BasePageLocators.LOGIN_SUBMIT)
        button_submit.click()





