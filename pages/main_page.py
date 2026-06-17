import allure
from pages.base_page import BasePage
from locators import MainPageLocators as MPL
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls


class MainPage(BasePage):

    @allure.step('Открываем главную страницу.')
    def open_main_page(self):
        self.open_url(Urls.MAIN_URL)

    @allure.step('Принимаем куки.')
    def accept_cookies(self):
        self.click_element(MPL.COOKIE_BUTTON)

    def click_order_button_top(self):
        self.click_element(MPL.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть по нижней кнопке 'Заказать' со скроллом")
    def click_order_button(self):
        self.scroll_to_element(MPL.ORDER_BUTTON)
        self.click_element(MPL.ORDER_BUTTON)

    @allure.step("Кликнуть по вопросу аккордеона № {index}")
    def click_accordion_question(self, index):
        raw_xpath = f"{MPL.ACCORDION_QUESTION[1]}[{index + 1}]"
        locator = (By.XPATH, raw_xpath)
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step("Взять текст ответа из аккордеона № {index}")
    def get_accordion_answer_text(self, index):
        raw_xpath = f"{MPL.ACCORDION_ANSWER[1]}[{index + 1}]"
        locator = (By.XPATH, raw_xpath)
        return self.get_text(locator)

    def click_scooter_logo(self):
        self.click_element(MPL.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу 'Яндекс', перейти на Дзен и получить URL новой вкладки")
    def click_yandex_logo_and_get_url(self):
        self.click_element(MPL.YANDEX_LOGO)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.url_contains("dzen.ru"))
        return self.driver.current_url














