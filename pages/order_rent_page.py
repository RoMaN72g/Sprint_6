import allure
from pages.base_page import BasePage
from locators import OrderRentPageLocators as ORPL
from selenium.webdriver.common.by import By



class OrderRentPage(BasePage):

    @allure.step("Заполнение даты привоза самоката")
    def date_choose(self):
        self.click_element(ORPL.DATE_INPUT)
        self.click_element(ORPL.NEXT_DAY)

    @allure.step("Выбор срока аренды: {rent_time}")
    def choose_rent_time(self, rent_time):
        self.click_element(ORPL.RENTAL_PERIOD)
        raw_xpath = ORPL.RENTAL_OPTION.replace('{rent_time}', rent_time)
        target_locator = (By.XPATH, raw_xpath)
        self.click_element(target_locator)

    @allure.step("Выбор цвета самоката: {scooter_color}")
    def select_scooter_color(self, scooter_color):
        raw_xpath = ORPL.SCOOTER_COLOR_OPTION.replace('{scooter_color}', scooter_color)
        target_locator = (By.XPATH, raw_xpath)
        self.click_element(target_locator)

    @allure.step("Ввод комментария для курьера")
    def input_comment(self, text="жду"):
        self.send_keys(ORPL.COMMENT_INPUT, text)

    def click_order_button(self):
        self.click_element(ORPL.ORDER_SUBMIT_BUTTON)

    @allure.step("Финальное подтверждение заказа (клик 'Да' в поп-апе)")
    def click_confirm_yes_button(self):
        self.click_element(ORPL.YES_BUTTON)

    @allure.step("Проверить, что появилось всплывающее окно 'Заказ оформлен'")
    def is_view_status_button_displayed(self):
        element = self.find_element(ORPL.VIEW_ORDER_BUTTON)
        return element.is_displayed()





