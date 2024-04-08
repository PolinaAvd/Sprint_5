from locators import Locators
import settings

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestExit():
    def test_vihod_iz_lichn_kab_successful_exit(self, driver):
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(settings.email)
        driver.find_element(*Locators.PASS).send_keys(settings.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.VISIBLE_COMPONENT_ON_MAIN))
        driver.find_element(*Locators.LICHN_KABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SOHRANIT_V_LICHN_KAB))
        driver.find_element(*Locators.KNOPKA_EXIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        assert driver.current_url == settings.URL + "/login"
        driver.quit()
