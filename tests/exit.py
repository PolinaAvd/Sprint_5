
from locators import Locators
import settings

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestExit():
    def test_vihod_iz_lichn_kab_successful_exit(self, driver, email, password):
        driver.get(settings.URL + "/login")
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email['mail'])
        driver.find_element(*Locators.PASS).send_keys(password['pass'])
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.VISIBLE_COMPONENT_ON_MAIN))
        assert driver.current_url == settings.URL + "/"
        driver.find_element(*Locators.LICHN_KABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SOHRANIT_V_LICHN_KAB))
        assert driver.current_url == settings.URL + '/account/profile'
        driver.find_element(*Locators.KNOPKA_EXIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        assert driver.current_url == settings.URL + "/login"
        driver.quit()
