import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Настраиваем браузер перед тестом
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    # Обязательно закрываем после теста
    chrome_driver.quit()


def test_check_text_in_iframe(driver):
    # Шаг 1: Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    wait = WebDriverWait(driver, 10)

    # Шаг 2 & 3: Находим iframe  и переключаемся в него
    iframe_element = wait.until(EC.presence_of_element_located((By.ID, "my-iframe")))
    driver.switch_to.frame(iframe_element)


    content_locator = (By.CSS_SELECTOR, "#content")
    target_text = "semper posuere integer et senectus"

    # Шаг 4 Ждем, пока внутри элемента появится наш текст
    wait.until(EC.text_to_be_present_in_element(content_locator, target_text))
    # Теперь находим сам элемент, чтобы проверить его отображение через assert
    content_container = driver.find_element(*content_locator)

    # Шаг 5: Убедиться, что текст отображается на странице.
    assert content_container.is_displayed(), "Текст найден в коде, но не отображается на экране!"
    assert target_text in content_container.text, "Искомый текст отсутствует в контейнере!"
    print("\n[УСПЕХ] Selenium дождался появления текста внутри контейнера #content!")

    # Шаг 6: Возвращаемся на главную страницу
    driver.switch_to.default_content()