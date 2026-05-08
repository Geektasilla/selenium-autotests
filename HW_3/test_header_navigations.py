import pytest
from selenium import webdriver
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


def test_check_header_elements(driver):
    # Принимаем куки
    cookie = driver.find_element(By.CSS_SELECTOR, ".t972__accept-btn")
    cookie.click()
    time.sleep(1)

    # Логотип ITCareerHub
    logo = driver.find_element(By.CSS_SELECTOR, '#rec1921710463 .tn-atom img')
    assert logo.is_displayed()
    print("Логотип ICH отображается")

     # Программы
    program_link = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='#submenu:more']")
    assert  program_link.is_displayed()
    print("Ссылка 'Программы' отображается")

    # Онас
    about_link = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='#submenu:more2']")
    assert about_link.is_displayed()
    print("Ссылка 'О нас' отображается")

    # bildungsgutschein
    building_link = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='#submenu:more2']")
    assert building_link.is_displayed()
    print("Ссылка 'bildungsgutschein' отображается")

    # Отзывы
    reviews_link = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='/reviews']")
    assert reviews_link.is_displayed()
    print("Ссылка 'Отзывы' отображается")

    # Блог
    blog_link = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='https://blog.itcareerhub.de/']")
    assert blog_link.is_displayed()
    print("Ссылка 'Блог' отображается")

    ru_button = driver.find_element(By.CSS_SELECTOR, '#rec1921710463 a[href="/ru"]')
    assert  ru_button.is_displayed()
    print("Кнопка 'ru' отображается")


    de_button = driver.find_element(By.CSS_SELECTOR, '.tn-elem__19217104631710153064158 a')
    assert  de_button.is_displayed()
    print("Кнопка 'de' отображается")