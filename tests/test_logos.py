import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage



@allure.title("Проверка логотипа 'Самокат'")
@allure.description("Проверяем, что при клике на логотип 'Самокат' из формы заказа происходит успешный возврат на главную страницу сайта.")
def test_click_scooter_logo_returns_to_main_page(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    order_page.open_order_page()
    main_page.click_scooter_logo()
    assert driver.current_url == main_page.MAIN_URL


@allure.title("Проверка логотипа 'Яндекс'")
@allure.description("Проверяем, что при клике на логотип 'Яндекс' в новой вкладке открывается главная страница Дзена.")
def test_click_yandex_logo_opens_dzen(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.click_yandex_logo_and_get_url()
    assert 'dzen.ru' in driver.current_url
