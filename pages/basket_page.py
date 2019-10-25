from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def clear_all(self):
        #если не пустая, очищаем
        if not self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT):
            button_clear = self.browser.find_element(*BasketPageLocators.BUTTON_CLEAR)
            button_clear.click()
            alert_win = self.browser.switch_to.alert
            alert_win.accept()

    def safe_order(self):
        button = self.browser.find_element(*BasketPageLocators.BUTTON_SAVE_ORDER)
        button.click()
