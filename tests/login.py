
from locators import Locators
import settings
import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestLogin():
    def test_successful_enter(self, driver, email, password):
        driver.get(settings.URL + "/login")
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email['mail'])
        driver.find_element(*Locators.PASS).send_keys(password['pass'])
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.VISIBLE_COMPONENT_ON_MAIN))
        assert driver.current_url == settings.URL + "/"
        driver.quit()
    def test_not_successful_enter_through_lichn_kab(self, driver):
        driver.get(settings.URL + "/login")
        driver.find_element(*Locators.LICHNIJ_KABINET).click()
        assert driver.current_url == settings.URL + "/login"
        driver.quit()

    def test_vosstan_pass_successful(self, driver, email):
        driver.get(settings.URL + "/login")
        driver.find_element(*Locators.LINK_VOSSTAN_PASS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.VOSSTAN_PASS))
        assert driver.current_url == settings.URL + '/forgot-password'
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email['mail'])
        driver.find_element(*Locators.VOSSTANOVIT_PASS).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.VVEDITE_KOD_IZ_PISMA))
        assert driver.current_url == settings.URL + '/reset-password'
        password = (f"Pass{random.randint(100, 999)}")
        driver.find_element(*Locators.VVEDITE_NOVIJ_PASS).send_keys(password)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('1111')
        driver.find_element(*Locators.SOHRANIT).click()
        driver.find_element(*Locators.KNOPKA_VOITI).click()
        assert driver.current_url == settings.URL + "/login"
        driver.quit()

