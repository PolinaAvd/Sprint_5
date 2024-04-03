import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

driver.find_element(By.XPATH, "./html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys('User')

email = f"polina_avdohina_k7_{random.randint(100, 999)}@gmail.com"
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(email)

password = f"Pass{random.randint(100, 999)}"
driver.find_element(By.XPATH, ".//div[@class='input__container']//input[@name='Пароль']").send_keys(password)

driver.find_element(By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Зарегистрироваться']").click()

(WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//main[@class='App_componentContainer__2JC2W']//h2[text()='Вход']"))))

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.find_element(By.XPATH, ".//div[@class='input__container']//input[@name='name']").send_keys(email)

driver.find_element(By.XPATH, "//div[@class='input__container']//input[@name='Пароль']").send_keys(password)

driver.find_element(By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//button[text()='Войти']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//main[@class='App_componentContainer__2JC2W']//h1[@class='text text_type_main-large mb-5 mt-10']")))

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

driver.quit()

