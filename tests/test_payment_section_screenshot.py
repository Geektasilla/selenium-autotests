from selenium.webdriver.common.by import By

PAYMENT_SECTION_ID = "rec1921734713"


def test_payment_section_screenshot(driver_on_home_page):
    driver = driver_on_home_page

    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()

    payment_section = driver.find_element(By.ID, PAYMENT_SECTION_ID)
    assert payment_section.is_displayed()

    payment_section.screenshot("screenshots/payment_methods.png")
