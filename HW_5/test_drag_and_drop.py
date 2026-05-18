import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_drag_and_drop(driver):
    # Шаг 1: Открыть страницу
    driver.get('https://www.globalsqa.com/demo-site/draganddrop/')
    wait = WebDriverWait(driver,10)

    # принимаем куки
    accept_cookie = driver.find_element(By.CSS_SELECTOR, 'p.fc-button-label')
    accept_cookie.click()

    # Переключаемся в iframe
    iframe_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(iframe_element)

    # Находим элемент, на который хотим навести курсор
    photo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#gallery>li:nth-child(1)')))

    # Находим корзину, куда будем тащить photo
    trash = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#trash')))

    # Захватить первую фотографию (верхний левый элемент).
    action = ActionChains(driver)
    action.drag_and_drop(photo, trash).perform()

    # Проверить, что после перемещения:
    # В корзине появилась одна фотография.
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    remaining_photos = driver.find_elements(By.CSS_SELECTOR, "#gallery > li")
    trash_photos = driver.find_elements(By.CSS_SELECTOR, "#trash li")

    # Проверки, что в основной области осталось 3 фотографии.
    assert len(remaining_photos) == 3, f"В галерее осталось: {len(remaining_photos)}"
    assert len(trash_photos) == 1, f"В корзине: {len(trash_photos)}"

    driver.switch_to.default_content()
