import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

driver.find_element(By.XPATH, "./html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys('User')

email = f"polina_avdohina_k7_{random.randint(100, 999)}@gmail.com"
driver.find_element(By.XPATH, "./html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(email)

driver.find_element(By.XPATH, "//div[@class='input__container']//input[@name='Пароль']").send_keys("1")

driver.find_element(By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//button[text()='Зарегистрироваться']").click()

WebDriverWait(driver, 3)

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

driver.quit()
