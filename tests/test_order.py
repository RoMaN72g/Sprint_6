import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.order_rent_page import OrderRentPage

@pytest.mark.parametrize(
    "name, last_name, address, metro_station, phone, scooter_color, rent_time",
    [
        # Юзер 1: Иван Иванов (Черкизовская, чёрный самокат, сутки)
        ("Иван", "Иванов", "ул. Ленина, д. 10", "Черкизовская", "89991112233", "чёрный", "сутки"),
        # Юзер 2: Петр Петров (Сокольники, серый самокат, двое суток)
        ("Петр", "Петров", "проспект Мира, д. 25", "Сокольники", "89154445566", "серая", "двое суток")
    ])

@allure.title("Сквозной процесс оформления заказа самоката")
@allure.description("Проверяем полный цикл заказа для двух разных пользователей станциями метро, сроками аренды и цветами самоката.")
def test_order_page(driver, name, last_name, address, metro_station, phone, scooter_color, rent_time):
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
    assert driver.current_url == order_page.ORDER_URL



