import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://itcareerhub.de/ru')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_navigation_about_to_contacts(driver):
    # 1. Принимаем куки
    cookie = driver.find_element(By.CSS_SELECTOR, ".t972__accept-btn")
    cookie.click()
    time.sleep(1)

    # ШАГ 1: Кликаем на раздел "О нас"
    # Твой селектор верный, он открывает выпадающее меню
    about_us = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='#submenu:more2']")
    about_us.click()

    time.sleep(2)
    # # ШАГ 2: Кликаем на раздел "Контакты"

    callback_btn = driver.find_element(By.CSS_SELECTOR, "div.t794__content a[href*='contact-us']")
    callback_btn.click()

    time.sleep(2)

    # Проверка (Assert) - всегда добавляем в конце!
    assert "/contact-us" in driver.current_url
    print("Успешно перешли на страницу Контакты!")

    time.sleep(3)

    # ШАГ 3: Скролл до кнопки
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    print("Прокрутили страницу вниз кнопкой клавиатуры")

    # ШАГ 4: Кликаем на "Обратный звонок"
    # На странице контактов ищем кнопку
    callback_btn = driver.find_element(By.LINK_TEXT, 'ОБРАТНЫЙ ЗВОНОК')
    callback_btn.click()
    time.sleep(2)

    # ШАГ 5: Проверка текста
    expected_text = "Запишитесь на бесплатную карьерную консультацию"
    txt_msg = driver.find_element(By.CSS_SELECTOR, "[field='tn_text_175871291756015470']")
    # molecule-175871291756044240 > div.t396__elem.tn-elem.t396__elem-flex.tn-elem__1862496483175871291756015470 > div

    assert txt_msg.is_displayed()
    assert expected_text in txt_msg.text

    print(f"Текст найден: {txt_msg.text}")






