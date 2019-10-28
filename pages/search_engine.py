from .locators import SearchLocators
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

    def is_pos_added_to_basket(self, rownum):
        locator_one_row = SearchLocators.SEARCH_ROWS + f"[{rownum}]"
        locator_action_ref = locator_one_row + '/td[contains(@class, "search-col__action")]//a'

        action_ref = self.browser.find_element(By.XPATH, locator_action_ref)
        action_classes = action_ref.get_attribute("class")

        return "add-basket__link--added" in action_classes


    def get_search_results(self):
        results = list()
        row_elements = self.browser.find_elements(By.XPATH, SearchLocators.SEARCH_ROWS)

        for i, r in enumerate(row_elements, 1):
            part_brand_name = r.get_attribute("data-brand-group")
            locator_one_row = SearchLocators.SEARCH_ROWS + f"[{i}]"
            locator_part_name = locator_one_row + '/td[contains(@class, "search-col__spare_info")]/p'
            locator_time = locator_one_row + '/td[contains(@class, "search-col__term_and_destination")]'
            locator_remains = locator_one_row + '/td[contains(@class, "search-col__remains")]'
            locator_price = locator_one_row + '/td[contains(@class, "search-col__final_price")]/nobr'
            locator_action_ref = locator_one_row + '/td[contains(@class, "search-col__action")]//a'

            #print(locator_one_row)
            #print(locator_part_name)
            dict_row = dict()

            try:
                part_name = self.browser.find_element(By.XPATH, locator_part_name).text
            except:
                pass

            part_del_terms = self.browser.find_element(By.XPATH, locator_time).text
            part_remains = self.browser.find_element(By.XPATH, locator_remains).text
            part_price = self.browser.find_element(By.XPATH, locator_price).get_attribute("data-price")
            part_added = self.is_pos_added_to_basket(i)

            dict_row.update({"pos": i})
            dict_row.update({"brand": part_brand_name})
            dict_row.update({"name": part_name})
            dict_row.update({"delivery_terms" : part_del_terms})
            dict_row.update({"remains" : part_remains})
            dict_row.update({"price" : part_price})
            dict_row.update({"inbasket" : part_added})

            results.append(dict_row)

        return results

    def add_to_basket(self, pos_num):
        locator_one_row = SearchLocators.SEARCH_ROWS + f"[{pos_num}]"
        locator_action_ref = locator_one_row + '/td[contains(@class, "search-col__action")]//a'

        #print(locator_action_ref)

        action_ref = self.browser.find_element(By.XPATH, locator_action_ref)
        action_classes = action_ref.get_attribute("class")

        #уже добавлено!
        if "add-basket__link--added" in action_classes:
            #print ("Уже добавлено!")
            pass
        else:
            action_ref.click()
            while not self.is_pos_added_to_basket(pos_num):
                pass



