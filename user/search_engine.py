from .locators import SearchLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchEngine():
    def __init__(self, browser):
        self.browser = browser

    def wait_for_search_results(self, timeout=20):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(SearchLocators.SEARCH_RESULTS))

    def search(self, what):
        time.sleep(1)
        elem = self.browser.find_element(*SearchLocators.SEARCH_INPUT)
        elem.send_keys(what)
        elem = self.browser.find_element(*SearchLocators.SEARCH_BUTTON)
        elem.click()
        self.wait_for_search_results()

    def is_pos_added_to_basket(self, row_num):
        locators = SearchLocators()

        action_ref = self.browser.find_element(*locators.get_basket_button(row_num))
        action_classes = action_ref.get_attribute("class")

        return "add-basket__link--added" in action_classes

    def found_something(self):
        try:
            self.browser.find_element(*SearchLocators.NOT_FOUND_WARN)
            return False
        except:
            return True

    def get_search_results(self):
        results = list()

        if not self.found_something():
            print ("Нет результата поиска")
            return results

        row_elements = self.browser.find_elements(*SearchLocators.SEARCH_ROWS)
        search_locators = SearchLocators()

        for i, r in enumerate(row_elements, 1):
            part_brand_name = r.get_attribute(SearchLocators.BRAND_NAME_ATT)

            try:
                part_name = self.browser.find_element(*search_locators.get_part_name(i)).text
            except:
                pass

            part_del_terms = self.browser.find_element(*search_locators.get_delivery_terms(i)).text
            part_remains = self.browser.find_element(*search_locators.get_remains(i)).text
            part_price = self.browser.find_element(*search_locators.get_price(i)).get_attribute(SearchLocators.PRICE_ATT)
            part_added = self.is_pos_added_to_basket(i)

            dict_row = dict()
            dict_row.update({"pos": i})
            dict_row.update({"brand": part_brand_name})
            dict_row.update({"name": part_name})
            dict_row.update({"delivery_terms" : part_del_terms})
            dict_row.update({"remains" : part_remains})
            dict_row.update({"price" : part_price})
            dict_row.update({"inbasket" : part_added})

            results.append(dict_row)

        return results

    def add_to_basket(self, row_num, qty = 1):
        if self.is_pos_added_to_basket(row_num):
            return

        locators = SearchLocators()

        qty_txt = self.browser.find_element(*locators.get_qty(row_num))
        qty_txt.clear()
        qty_txt.send_keys(str(qty))

        action_ref = self.browser.find_element(*locators.get_basket_button(row_num))
        action_ref.click()

        while not self.is_pos_added_to_basket(row_num):
            pass



