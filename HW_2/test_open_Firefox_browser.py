import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()

def test_payment_section_screenshot(driver):
    about_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    about_link.click()
    sleep(3)
    # Делаем скриншот всего окна, если будет то включая  и меню. Но это неправильно.
    # Просто в данном случае их нет и как буд-то этот вариант тоже подойдет.
    driver.save_screenshot("A_QA/HW/HW_2/payment_methods.png")

    # Правильный вариант. Делаем скриншот ТОЛЬКО этой секции как по заданию.
    # payment_section = driver.find_element(By.ID, "rec1921734713")
    # payment_section.screenshot("A_QA/HW/HW_2/payment_methods.png")
    sleep(2)

