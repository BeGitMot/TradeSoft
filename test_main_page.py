from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.search_engine import SearchEngine
from .pages.make_order_page import MakeOrderPage

import time

MAIN_URL = "http://etspru-test.auto-vision.ru"

def test_tradesoft_main_page(browser):
    #открываем страницу
    main_page = MainPage(browser, MAIN_URL)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    main_page.open()

    # входим
    main_page.open_login_form()
    main_page.login("plyush_dv@etsp.ru", "121524")

    #поиск
    time.sleep(1)
    search_engine = SearchEngine(browser)
    search_engine.start_search("8GH007157121")
    search_engine.wait_for_search_results()
    search_results = search_engine.get_search_results()
    #print(search_results)

    #добавляем все в корзину
    for i, r in enumerate(search_results, 1):
        search_engine.add_to_basket(i)

    #time.sleep(3)

    main_page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.safe_order()

    make_order_page = MakeOrderPage(browser, browser.current_url)
    make_order_page.fill_order_form()
    make_order_page.confirm_order()

    #time.sleep(3)
    #basket_page.clear_all()
    #time.sleep(5)
    #basket_page.clear_all()
    #//tr[contains(@class, "search-code-row")][2]/td[contains(@class, "search-col__action")]/td[contains(@class, "search-col__action")]//a
    time.sleep(60000)
