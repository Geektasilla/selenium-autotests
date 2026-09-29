from selenium.webdriver.common.by import By

HEADER = "#rec1921710463"


def test_check_header_elements(driver_on_home_page):
    driver = driver_on_home_page

    logo = driver.find_element(By.CSS_SELECTOR, f"{HEADER} .tn-atom img")
    assert logo.is_displayed()

    program_link = driver.find_element(By.CSS_SELECTOR, f"{HEADER} a[href='#submenu:more']")
    assert program_link.is_displayed()

    about_link = driver.find_element(By.CSS_SELECTOR, f"{HEADER} a[href='#submenu:more2']")
    assert about_link.is_displayed()

    building_link = driver.find_element(By.CSS_SELECTOR, f"{HEADER} a[href*='bildungsgutschein']")
    assert building_link.is_displayed()

    reviews_link = driver.find_element(By.CSS_SELECTOR, f"{HEADER} a[href='/reviews']")
    assert reviews_link.is_displayed()

    blog_link = driver.find_element(By.CSS_SELECTOR, f"{HEADER} a[href='https://blog.itcareerhub.de/']")
    assert blog_link.is_displayed()

    ru_button = driver.find_element(By.CSS_SELECTOR, f"{HEADER} a[href='/ru']")
    assert ru_button.is_displayed()

    de_button = driver.find_element(By.CSS_SELECTOR, ".tn-elem__19217104631710153064158 a")
    assert de_button.is_displayed()
