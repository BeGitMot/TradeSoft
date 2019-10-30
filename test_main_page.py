from common.common import connect_to_browser
from user.main_page import MainPage
from user.search_engine import SearchEngine
from user.basket_page import BasketPage
from user.make_order_page import MakeOrderPage
from user.orders_page import OrdersPage
from admin.admin_main_page import AdminMainPage
from selenium import webdriver
import time


ADMIN_MAIN_URL = "http://etspru-test.auto-vision.ru/admin"

def OFF_test_tradesoft_admin_pages():
    browser = connect_to_browser("firefox")
    #admin_main_page = AdminMainPage(browser, ADMIN_MAIN_URL)
    #admin_main_page.open()
    #time.sleep(60000)
    #time.sleep(30)
    admin_main_page = AdminMainPage(browser, ADMIN_MAIN_URL)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    admin_main_page.open()
    time.sleep(2)
    #admin_main_page.login("admin", "bulka1983")


    #admin_main_page.accept_alert()
    #admin_main_page.login("admin", "bulka1983")

    time.sleep(30)


MAIN_URL = "http://etspru-test.auto-vision.ru"

def test_tradesoft_user_pages():
    browser = connect_to_browser("firefox")
    #browser = webdriver.Chrome()

    #открываем страницу
    main_page = MainPage(browser, MAIN_URL)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    main_page.open()

    # входим
    #time.sleep(2)
    main_page.open_login_form()
    main_page.login("plyush_dv@etsp.ru", "121524")

    #поиск
    search_engine = SearchEngine(browser)
    time.sleep(1)
    search_engine.search("8GH007157121")
    search_results = search_engine.get_search_results()
    #print(search_results)

    #добавляем все в корзину
    for i, r in enumerate(search_results, 1):
        search_engine.add_to_basket(i, 3)

    #time.sleep(3)
    main_page.go_to_basket_page()
    #basket_page = BasketPage(browser, browser.current_url)
    #basket_page.clear_all()
    #time.sleep(2)
    
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.safe_order()
    
    make_order_page = MakeOrderPage(browser, browser.current_url)
    make_order_page.fill_order_form()
    make_order_page.confirm_order()

    time.sleep(2)
    main_page.go_to_orders_page()
    time.sleep(2)
    orders_page = OrdersPage(browser, browser.current_url)
    orders_items = orders_page.get_positions()

    for i, item in enumerate(orders_items, 1):
        if item["status"] == "заказ принят":
            orders_page.mark_position(i)

    #orders_page.mark_position(5)
    orders_page.cancel_marked_positions()

    # time.sleep(60000)

    browser.quit()

