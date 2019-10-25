from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[data-role = "open-auth-form"]>span')