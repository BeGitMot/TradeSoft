from common.common import CommonPage

class AdminBasePage(CommonPage):
    def login(self, name, password):
        pass
        '''
        elem = self.browser.find_element(*BasePageLocators.LOGIN_NAME)
        elem.send_keys(name)

        elem = self.browser.find_element(*BasePageLocators.LOGIN_PASSWORD)
        elem.send_keys(password)

        button_submit = self.browser.find_element(*BasePageLocators.LOGIN_SUBMIT)
        button_submit.click()
        '''









