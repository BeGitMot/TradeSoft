from .base_page import BasePage
from .locators import OrdersPageLocators

class OrdersPage(BasePage):
    def get_positions(self):
        def ftxt(f, n):
            return self.browser.find_element(*f(n)).text

        results = list()
        row_elements = self.browser.find_elements(*OrdersPageLocators.POS_ROWS)
        locators = OrdersPageLocators()

        for i, r in enumerate(row_elements, 1):
            dict_row = dict()
            dict_row.update({"pos": i})
            dict_row.update({"orderid": ftxt(locators.get_order_id, i)})
            dict_row.update({"status": ftxt(locators.get_status, i)})
            dict_row.update({"name": ftxt(locators.get_part_name, i)})
            dict_row.update({"delivery_terms": ftxt(locators.get_delivery_time, i)})
            dict_row.update({"partnum": ftxt(locators.get_part_num, i)})
            dict_row.update({"brand": ftxt(locators.get_part_brand, i)})
            dict_row.update({"price": ftxt(locators.get_price, i)})
            dict_row.update({"qty": ftxt(locators.get_part_qty, i)})
            dict_row.update({"amount": ftxt(locators.get_amount, i)})


            results.append(dict_row)

        return results

    def mark_position(self, index):
        locators = OrdersPageLocators()
        mark_elem = self.browser.find_element(*locators.get_mark(index))
        self.click_by_java_script(mark_elem)#не работает обычный клик

    def cancel_marked_positions(self):
        cancel_button = self.browser.find_element(*OrdersPageLocators.CANCEL_BUTTON)
        cancel_button.click()
        self.accept_alert()
        self.wait_for_visibility(OrdersPageLocators.CANCEL_SUCCESS_MSG, 10)


