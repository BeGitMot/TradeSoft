from .admin_base_page import AdminBasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

class AdminMainPage(AdminBasePage):
    def __init__(self, *args, **kwargs):
        super(AdminMainPage, self).__init__(*args, **kwargs)

    def login(self, name, password):
        alert = self.browser.switch_to.alert
        #alert.send_keys(f'{name}{Keys.TAB}{password}')
        alert.send_keys('qweqwe')
        alert.accept()


