from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "header__user-info") and not(contains(@class, "mobile"))]//button')


    LOGIN_NAME = (By.CSS_SELECTOR, 'input[name = "login"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[name = "password"]')
    LOGIN_SUBMIT = (By.CSS_SELECTOR, 'button.auth-block__button_submit[type = "submit"]')
    BASKET_REF = (By.XPATH, '//a[@data-field="module-basket"]')
    ORDERS_REF = (By.XPATH, '//*[@id="page"]/div[3]/div/div/div/div/div[2]/a[1]')

class SearchLocators():
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input.search-form__input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[name="search"]')
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'div.search-data__title')
    SEARCH_ROWS = (By.XPATH, '//tr[contains(@class, "search-code-row")]')
    BRAND_NAME_ATT = "data-brand-group"
    PRICE_ATT  = "data-price"

    def get_row_by_num(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], SearchLocators.SEARCH_ROWS[1] + f"[{rownum}]")

    def get_part_name(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '/td[contains(@class, "search-col__spare_info")]/p')

    def get_delivery_terms(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '/td[contains(@class, "search-col__term_and_destination")]')

    def get_remains(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '/td[contains(@class, "search-col__remains")]')

    def get_price(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '/td[contains(@class, "search-col__final_price")]/nobr')

    def get_qty(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '/td[contains(@class, "search-col__action")]//input[contains(@class, "DigitalTextBox")]')

    def get_basket_button(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '/td[contains(@class, "search-col__action")]//a')


class BasketPageLocators():
    BUTTON_CLEAR = (By.CSS_SELECTOR, 'button.basket-page__cancel-button')
    BUTTON_SAVE_ORDER = (By.CSS_SELECTOR, 'input[name="save_order"]')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, 'h2.basket-page__empty-slogan')

class MakeOrderPageLocators():
    SELECT_TERM = (By.CSS_SELECTOR, '#ord_pmk_id')
    BUTTON_CONFIRM = (By.CSS_SELECTOR, 'input[name = "save_order"]')

class OrdersPageLocators():
    POS_ROWS = (By.XPATH, '//tr[contains(@class, "positions-table__tr")]')
    CANCEL_BUTTON = (By.CSS_SELECTOR, 'input.positions-page__cancel-button')
    CANCEL_SUCCESS_MSG = (By.CSS_SELECTOR, 'div.message_type_success')

    def get_row_by_num(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], OrdersPageLocators.POS_ROWS[1] + f"[{rownum}]")

    def get_mark(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//input[@name="cancelPos"]')

    def get_status(self, rownum):
        #return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '/td[1]/div/div[2]')
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//div[@class="stt-name-info__status-title"]')

    def get_part_name(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//td[2]/div[1]')

    def get_part_qty(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//td[2]/div[2]')

    def get_part_brand(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//td[3]/div[1]')

    def get_part_num(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//td[3]/div[2]')

    def get_delivery_time(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//td[4]/div[1]')

    def get_supplier(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//td[4]/div[2]')

    def get_price(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//td[5]//span')

    def get_amount(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//td[6]/div[1]/span')

    def get_order_id(self, rownum):
        return (SearchLocators.SEARCH_ROWS[0], self.get_row_by_num(rownum)[1] + '//td[7]//a/nobr')



