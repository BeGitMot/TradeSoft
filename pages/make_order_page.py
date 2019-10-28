from .base_page import BasePage
from .locators import MakeOrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class MakeOrderPage(BasePage):
    def fill_order_form(self):
        #условия оплаты
        sel = Select(self.browser.find_element(*MakeOrderPageLocators.SELECT_TERM))
        sel.select_by_value("2")

    def confirm_order(self):
        butt = self.browser.find_element(*MakeOrderPageLocators.BUTTON_CONFIRM)
        butt.click()

