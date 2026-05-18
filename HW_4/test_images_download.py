import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_image_download_change(driver):
    """
    Проверка загрузки изображений.
    """
    wait = WebDriverWait(driver, 15)

    # 1. Ждем появления ВСЕХ картинок
    wait.until(EC.presence_of_element_located((By.ID, 'landscape')))
    print(f"Все картинки загружены")

    award_image = driver.find_element(By.ID, 'award')

    # 3. Вытаскиваем атрибут
    alt_text = award_image.get_attribute("alt")

    # 4. Проверяем, что значение атрибута alt равно "award".
    assert alt_text == "award", f"Ожидали award, получили {alt_text}"

    print(f"Атрибут alt третьей картинки: {alt_text}")

