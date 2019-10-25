from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class MakeOrderPage(BasePage):
    def fill_order_form(self):
        sel = Select(browser.find_element_by_id("dropdown"))
        sel.select_by_value(num_sum)

