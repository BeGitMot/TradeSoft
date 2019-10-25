from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[data-role = "open-auth-form"]')
    LOGIN_NAME = (By.CSS_SELECTOR, 'input[name = "login"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[name = "password"]')
    LOGIN_SUBMIT = (By.CSS_SELECTOR, 'button.auth-block__button_submit[type = "submit"]')

class SearchLocators():
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input.search-form__input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[name="search"]')
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'div.search-data__title')

