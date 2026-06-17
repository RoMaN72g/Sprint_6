from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    # Локатор для вопросов о важном
    ACCORDION_QUESTION = (By.XPATH, "(//div[contains(@id, 'accordion__heading')])")
    # Локатор для ответов
    ACCORDION_ANSWER = (By.XPATH, "(//div[contains(@id, 'accordion__panel')])")
    # Верхняя кнопка "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    # Нижняя кнопка "Заказать"
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    # Логотип "Яндекс"
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    # Логотип "Самокат"
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
class OrderPageLocators:
    # Плейсхолдер "Имя"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    # Плейсхолдер "Фамилия"
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Плейсхолдер "Адрес"
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Плейсхолдер "Станция метро"
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # Локатор станции метро
    METRO_STATION_OPTION = (By.XPATH, "//div[text()='")
    # Плейсхолдер "Телефон"
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка "Далее"
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
class OrderRentPageLocators:
    # Плейсхолдер "Когда привезти самокат"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Следующая дата в календаре
    NEXT_DAY = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]/following-sibling::div")
    # Плейсхолдер "Срок аренды"
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    # Выбор срока аренды
    RENTAL_OPTION = "//div[@class='Dropdown-option'][text()='{rent_time}']"
    # Выбор цвета сомаката
    SCOOTER_COLOR_OPTION = "//label[contains(text(), '{scooter_color}')]"
    # Плейсхолдер "Комментарий для курьера"
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка "Заказать" в форме про аренду
    ORDER_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Button')]//button[text()='Заказать']")
    # Кнопка "Да" в окне "Хотите оформить заказ"
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    # Кнопка "Посмотреть" на странице заказа
    VIEW_ORDER_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
