import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://uitestingplayground.com/textinput')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_change_text_button(driver):
    """
    Проверка изменения текста кнопки
    """
    # Вводим в поле ввода текст "ITCH".
    text_input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
    text_input.send_keys("ITCH")

    # Кликаем на синюю кнопку.
    new_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
    new_button.click()

    # Проверяем, что текст кнопки изменился на "ITCH".
    check_change = new_button.text
    # Сравниваем полученный текст с тем, что вводили
    assert check_change == "ITCH", f"Ожидали ITCH, но получили {check_change}"
    print(f"Текст успешно изменен на {check_change}")
