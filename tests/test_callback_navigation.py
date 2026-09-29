from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

POPUP_TEXT_FIELD = "[field='tn_text_175871291756015470']"
EXPECTED_POPUP_TEXT = "Запишитесь на бесплатную карьерную консультацию"


def _js_click(driver, element):
    """Some header buttons on this page overlap with animated blocks,
    which makes a native Selenium click intercepted. A JS click bypasses
    the overlay and reaches the actual element."""
    driver.execute_script("arguments[0].click();", element)


def test_navigation_about_to_contacts(driver_on_home_page):
    driver = driver_on_home_page
    wait = WebDriverWait(driver, 10)

    about_us = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='#submenu:more2']")
    about_us.click()

    contacts_link = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.t794__content a[href*='contact-us']"))
    )
    contacts_link.click()

    wait.until(EC.url_contains("/contact-us"))
    assert "/contact-us" in driver.current_url

    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)

    callback_btn = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "ОБРАТНЫЙ ЗВОНОК"))
    )
    _js_click(driver, callback_btn)

    popup_text = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, POPUP_TEXT_FIELD))
    )
    assert popup_text.is_displayed()
    assert EXPECTED_POPUP_TEXT in popup_text.text
