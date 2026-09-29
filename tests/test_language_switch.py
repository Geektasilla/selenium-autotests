from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DE_HEADING = "Erwerben Sie einen gefragten IT-Beruf und starten Sie Ihre Karriere in Deutschland"
RU_HEADING = "Освойте актуальные профессии в Германии"


def test_switch_languages_button(driver_on_home_page):
    driver = driver_on_home_page
    wait = WebDriverWait(driver, 10)

    de_button = driver.find_element(By.CSS_SELECTOR, ".tn-elem__19217104631710153064158 a")
    de_button.click()

    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "IT-Beruf"))
    assert driver.current_url == "https://itcareerhub.de/"
    heading_de = driver.find_element(By.TAG_NAME, "h1")
    assert DE_HEADING in heading_de.text

    ru_button = driver.find_element(By.CSS_SELECTOR, 'div[data-elem-id="176037137750141060"] a')
    ru_button.click()

    wait.until(EC.url_contains("/ru"))
    assert "itcareerhub.de/ru" in driver.current_url
    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), RU_HEADING))
    heading_ru = driver.find_element(By.TAG_NAME, "h1")
    assert RU_HEADING in heading_ru.text
