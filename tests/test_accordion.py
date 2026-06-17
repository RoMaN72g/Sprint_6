import pytest
import allure
from pages.main_page import MainPage
from data import AccordionData


@pytest.mark.parametrize(
    "index, expected_answer",
    [
        (0, AccordionData.ANSWERS[0]),
        (1, AccordionData.ANSWERS[1]),
        (2, AccordionData.ANSWERS[2]),
        (3, AccordionData.ANSWERS[3]),
        (4, AccordionData.ANSWERS[4]),
        (5, AccordionData.ANSWERS[5]),
        (6, AccordionData.ANSWERS[6]),
        (7, AccordionData.ANSWERS[7]),

    ]
)

@allure.title("Проверка выпадающего списка в разделе 'Вопросы о важном'")
@allure.description("Тестируем по очереди все 8 вопросов аккордеона. Проверяем, что при клике на стрелочку открывается правильный текст ответа, соответствующий требованиям.")
def test_accordion_questions_and_answers(driver, index, expected_answer):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.accept_cookies()
    main_page.click_accordion_question(index)
    actual_answer = main_page.get_accordion_answer_text(index)

    assert actual_answer == expected_answer

