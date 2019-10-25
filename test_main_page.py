from .pages.main_page import MainPage
import time

MAIN_URL = "http://etspru-test.auto-vision.ru"

def test_tradesoft_main_page(browser):
    page = MainPage(browser, MAIN_URL)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    time.sleep(3)
    page.go_to_login_page()
    time.sleep(6000)