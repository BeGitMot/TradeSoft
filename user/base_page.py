from .locators import BasePageLocators
from common.common import CommonPage

class BasePage(CommonPage):
    def open_login_form(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        link.click()

    def login(self, name, password):
        elem = self.browser.find_element(*BasePageLocators.LOGIN_NAME)
        elem.send_keys(name)

        elem = self.browser.find_element(*BasePageLocators.LOGIN_PASSWORD)
        elem.send_keys(password)

        button_submit = self.browser.find_element(*BasePageLocators.LOGIN_SUBMIT)
        button_submit.click()

    def go_to_basket_page(self):
        ref = self.browser.find_element(*BasePageLocators.BASKET_REF)
        ref.click()

    def go_to_orders_page(self):
        ref = self.browser.find_element(*BasePageLocators.ORDERS_REF)
        ref.click()








