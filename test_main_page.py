from .pages.main_page import MainPage
from .pages.search_engine import SearchEngine

import time

MAIN_URL = "http://etspru-test.auto-vision.ru"

def test_tradesoft_main_page(browser):
    #открываем страницу
    page = MainPage(browser, MAIN_URL)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()

    # входим
    page.open_login_form()
    page.login("plyush_dv@etsp.ru", "121524")

    #поиск
    time.sleep(1)
    search_engine = SearchEngine(browser)
    search_engine.start_search("8GH007157121")
    search_engine.wait_for_search_results()
    search_results = search_engine.get_search_results()
    #print(search_results)

    search_engine.add_to_basket(2)
    #//tr[contains(@class, "search-code-row")][2]/td[contains(@class, "search-col__action")]/td[contains(@class, "search-col__action")]//a
    #time.sleep(60000)
