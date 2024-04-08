from locators import Locators
import settings

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestRegistration():
    def test_link_to_registaration_successful_registration(self, driver):
        driver.find_element(*Locators.REG_LOC).click()
        driver.find_element(*Locators.NAME).send_keys(settings.user)
        email = settings.email_random
        driver.find_element(*Locators.EMAIL).send_keys(email)
        password = settings.password_random
        driver.find_element(*Locators.PASS).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTRANCE_BUTTON))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASS_FIELD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.VISIBLE_COMPONENT_ON_MAIN))
        assert driver.current_url == (settings.URL + "/")
        driver.quit()

    def test_link_to_registaration_too_short_pass_fail_registration(self, driver):
        driver.find_element(*Locators.REG_LOC).click()
        driver.find_element(*Locators.NAME).send_keys(settings.user)
        driver.find_element(*Locators.EMAIL).send_keys(settings.email_random)
        driver.find_element(*Locators.PASS).send_keys("1")
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3)
        assert driver.current_url == settings.URL + "/register"
        driver.quit()


