import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

driver.find_element(By.XPATH, ".//html/body/div/div/main/div/div/p[2]/a").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//main[@class='App_componentContainer__2JC2W']//h2[text()='Восстановление пароля']")))

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'

driver.find_element(By.XPATH, ".//div[@class='input__container']//input[@name='name']").send_keys("polina_avdohina_k7_077@gmail.com")

driver.find_element(By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Восстановить']").click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class='input__container']//label[text()='Введите код из письма']")))

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'

password = f"Pass{random.randint(100, 999)}"
driver.find_element(By.XPATH, "//div[@class='input__container']//input[@name='Введите новый пароль']").send_keys(password)

driver.find_element(By.XPATH, "//div[@class='input__container']//input[@name='name']").send_keys('1111')

driver.find_element(By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Сохранить']").click()

driver.find_element(By.XPATH, "//html/body/div/div/main/div/div/p/a").click()

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()

