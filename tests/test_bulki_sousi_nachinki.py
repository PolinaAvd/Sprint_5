from locators import Locators
import settings

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestTabs():
    def test_tabs_na_glavnoj_stranice_nachinki_successful_tabbing(self, driver):
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(settings.email)
        driver.find_element(*Locators.PASS).send_keys(settings.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.VISIBLE_COMPONENT_ON_MAIN))
        driver.find_element(*Locators.NACHINKI).click()
        elementOne = driver.find_element(*Locators.NACHINKI_ELEMENT_ONE)
        elementTwo = driver.find_element(*Locators.ELEMENT_TWO)
        assert elementOne == elementTwo
        driver.quit()

    def test_tabs_na_glavnoj_stranice_sousi_successful_tabbing(self, driver):
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(settings.email)
        driver.find_element(*Locators.PASS).send_keys(settings.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.VISIBLE_COMPONENT_ON_MAIN))
        driver.find_element(*Locators.SOUSI).click()
        elementOne = driver.find_element(*Locators.SOUSI_ELEMENT_ONE)
        elementTwo = driver.find_element(*Locators.ELEMENT_TWO)
        assert elementOne == elementTwo
        driver.quit()


    def test_tabs_na_glavnoj_stranice_bulki_successful_tabbing(self, driver):
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(settings.email)
        driver.find_element(*Locators.PASS).send_keys(settings.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.VISIBLE_COMPONENT_ON_MAIN))
        driver.find_element(*Locators.SOUSI).click()
        driver.find_element(*Locators.BULKI).click()
        elementOne = driver.find_element(*Locators.BULKI_ELEMENT_ONE)
        elementTwo = driver.find_element(*Locators.ELEMENT_TWO)
        assert elementOne == elementTwo
        driver.quit()

