from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import platform

class CommonPage:
    def __init__(self, browser, url, timeout=0):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def scroll_to_elem(self, elem):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", elem)

    def click_by_java_script(self, elem):
        self.browser.execute_script("arguments[0].click()", elem)

    def wait_for_visibility(self, loc, timeout = 2):
        WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(loc))

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def accept_alert(self):
        alert_win = self.browser.switch_to.alert
        alert_win.accept()


def connect_to_browser(browser_name = "chrome"):
    browser = None
    print(f"\nPlatform: {platform.system()}")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        if platform.system() == "Linux":
            browser = webdriver.Firefox(executable_path=r'/home/begemot/firefoxdriver/geckodriver')
        else:
            browser = webdriver.Firefox()

    else:
        raise Exception("browser_name should be chrome or firefox")

    return browser

    #print("\nquit browser..")

    #browser.quit()