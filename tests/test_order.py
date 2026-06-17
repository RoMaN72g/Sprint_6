import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.order_rent_page import OrderRentPage
from urls import Urls
from data import OrderData


@pytest.mark.parametrize(
    "name, last_name, address, metro_station, phone, rent_time, scooter_color",
    [
        OrderData.USER_1,
        OrderData.USER_2
    ]
)

@allure.title("Сквозной процесс оформления заказа самоката")
@allure.description("Проверяем полный цикл заказа для двух разных пользователей станциями метро, сроками аренды и цветами самоката.")
def test_order_page(driver, name, last_name, address, metro_station, phone, rent_time, scooter_color):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    order_rent_page = OrderRentPage(driver)
    main_page.open_main_page()
    main_page.accept_cookies()
    main_page.click_order_button_top()
    order_page.input_name(name)
    order_page.input_surname(last_name)
    order_page.input_address(address)
    order_page.input_station(metro_station)
    order_page.input_phone(phone)
    order_page.click_next_button()
    order_rent_page.date_choose()
    order_rent_page.choose_rent_time(rent_time)
    order_rent_page.select_scooter_color(scooter_color)
    order_rent_page.input_comment()
    order_rent_page.click_order_button()
    order_rent_page.click_confirm_yes_button()

    assert order_rent_page.is_view_status_button_displayed()



@allure.title("Проверка перехода по нижней кнопке 'Заказать'")
@allure.description("Проверяем, что клик по нижней кнопке 'Заказать' со скроллом успешно открывает стартовую форму оформления заказа.")
def test_bottom_order_button_opens_form(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    main_page.open_main_page()
    main_page.accept_cookies()
    main_page.click_order_button()
    assert order_page.get_current_url() == Urls.ORDER_URL



