from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[data-role = "open-auth-form"]')
    LOGIN_NAME = (By.CSS_SELECTOR, 'input[name = "login"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[name = "password"]')
    LOGIN_SUBMIT = (By.CSS_SELECTOR, 'button.auth-block__button_submit[type = "submit"]')
    BASKET_REF = (By.XPATH, '//a[@data-field="module-basket"]')

class SearchLocators():
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input.search-form__input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[name="search"]')
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'div.search-data__title')

class BasketPageLocators():
    BUTTON_CLEAR = (By.CSS_SELECTOR, 'button.basket-page__cancel-button')
    BUTTON_SAVE_ORDER = (By.CSS_SELECTOR, 'button[name="save_order"]')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, 'h2.basket-page__empty-slogan')

class MakeOrderLocators():
    SELECT_TERM = (By.CSS_SELECTOR, 'button.dropdown-toggle[data-id="term"]')


