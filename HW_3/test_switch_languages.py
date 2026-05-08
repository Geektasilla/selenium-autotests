import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://itcareerhub.de/ru')
    yield driver
    driver.quit()


def test_switch_languages_button(driver):
    """
    Проверка переключения языка.
    """
    # Принимаем куки
    cookie = driver.find_element(By.CSS_SELECTOR, ".t972__accept-btn")
    cookie.click()
    time.sleep(1)

    # 1.Step: Кликаем на кнопку смены языка на DE
    de_button = driver.find_element(By.CSS_SELECTOR, '.tn-elem__19217104631710153064158 a')
    de_button.click()

    time.sleep(3)

    # 2.Step: Проверяем, что URL и  заголовок изменились
    assert driver.current_url == "https://itcareerhub.de/"
    assert "itcareerhub.de/" in driver.current_url

    # 3.Step: Ищем заголовок
    heading_de = driver.find_element(By.TAG_NAME, 'h1')
    expected_part = "Erwerben Sie einen gefragten IT-Beruf und starten Sie Ihre Karriere in Deutschland"
    assert expected_part in heading_de.text
    print("Переключились на немецкий: заголовок и URL верные")

    time.sleep(5)

    # 4.Step: Переходим обратно на русский
    # Ищем кнопку заново, так как страница обновилась.

    # тут конечно надо было подумать)))))
    # ru_button = driver.find_element(By.XPATH, "//a[contains(@href, '/ru') and contains(text(), 'ru')]")
    ru_button = driver.find_element(By.CSS_SELECTOR, 'div[data-elem-id="176037137750141060"] a')
    ru_button.click()

    time.sleep(5)

    # 5. Step: Проверка русского URL
    assert "itcareerhub.de/ru" in driver.current_url.strip()
    assert "/ru" in driver.current_url.strip()

    heading_final = driver.find_element(By.TAG_NAME, 'h1')
    assert "Начните IT карьеру" in heading_final.text
    print("Переключились на русскую версию сайта: заголовок и URL верные")







