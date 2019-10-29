from selenium.webdriver.common.by import By

class AdminBasePageLocators():
    TMP_LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "header__user-info") and not(contains(@class, "mobile"))]//button')

