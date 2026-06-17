import allure
from pages.base_page import BasePage
from locators import OrderPageLocators as OPL
from selenium.webdriver.common.by import By
from urls import Urls


class OrderPage(BasePage):

    @allure.step("Открыть страницу оформления заказа.")
    def open_order_page(self):
        self.open_url(Urls.ORDER_URL)

    @allure.step("Ввод имени: {name}")
    def input_name(self, name):
        self.send_keys(OPL.NAME_INPUT, name)

    @allure.step("Ввод фамилии: {last_name}")
    def input_surname(self, last_name):
        self.send_keys(OPL.SURNAME_INPUT, last_name)

    @allure.step("Ввод адреса: {address}")
    def input_address(self, address):
        self.send_keys(OPL.ADDRESS_INPUT, address)

    @allure.step("Выбор станции метро: {metro_station}")
    def input_station(self, metro_station):
        self.click_element(OPL.METRO_INPUT)
        self.send_keys(OPL.METRO_INPUT, metro_station)
        raw_xpath = f"{OPL.METRO_STATION_OPTION[1]}{metro_station}']"
        target_locator = (By.XPATH, raw_xpath)
        self.click_element(target_locator)

    @allure.step("Ввод номера телефона: {phone}")
    def input_phone(self, phone):
        self.send_keys(OPL.PHONE_INPUT, phone)

    def click_next_button(self):
        self.click_element(OPL.NEXT_BUTTON)



