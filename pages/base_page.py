from .locators import BasePageLocators

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def scroll_to_elem(self, elem):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", elem)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        link.click()