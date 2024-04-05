import time
from selenium.webdriver.common.by import By

from locators import Locators
import settings

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestTabs():
    def test_tabs_na_glavnoj_stranice_successful_tabbing(self, driver, email, password):
        driver.get(settings.URL + "/login")
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email['mail'])
        driver.find_element(*Locators.PASS).send_keys(password['pass'])
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.VISIBLE_COMPONENT_ON_MAIN))
        assert driver.current_url == settings.URL + "/"
        driver.find_element(*Locators.NACHINKI).click()
        time.sleep(2)
        elementOne = driver.find_element(*Locators.NACHINKI_EL_ONE)
        elementTwo = driver.find_element(*Locators.EL_TWO)
        assert elementOne == elementTwo
        driver.find_element(*Locators.SOUSI).click()
        WebDriverWait(driver, 3)
        time.sleep(2)
        elementOne = driver.find_element(*Locators.SOUSI_EL_ONE)
        elementTwo = driver.find_element(*Locators.EL_TWO)
        assert elementOne == elementTwo
        driver.find_element(*Locators.BULKI).click()
        WebDriverWait(driver, 3)
        time.sleep(2)
        elementOne = driver.find_element(*Locators.BULKI_EL_ONE)
        elementTwo = driver.find_element(*Locators.EL_TWO)
        assert elementOne == elementTwo
        driver.quit()

