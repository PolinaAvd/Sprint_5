import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

driver.find_element(By.XPATH, ".//div[@class='input__container']//input[@name='name']").send_keys("polina_avdohina_k7_077@gmail.com")

driver.find_element(By.XPATH, ".//div[@class='input__container']//input[@name='Пароль']").send_keys("Gitera")

driver.find_element(By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Войти']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//main[@class='App_componentContainer__2JC2W']//h1[@class='text text_type_main-large mb-5 mt-10']")))

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

driver.find_element(By.XPATH, ".//div[@style='display: flex;']//span[text()='Начинки']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "./html/body/div/div/main/section[1]/div[2]/h2[3]")))
time.sleep(2)
element = driver.find_element(By.XPATH, "./html/body/div/div/main/section[1]/div[2]/h2[3]")

assert 'Начинки' in element.text

driver.find_element(By.XPATH, ".//div[@style='display: flex;']//span[text()='Соусы']").click()

WebDriverWait(driver, 3)
time.sleep(2)
element = driver.find_element(By.XPATH, "./html/body/div/div/main/section[1]/div[2]/h2[2]")

assert 'Соусы' in element.text

driver.find_element(By.XPATH, ".//div[@style='display: flex;']//span[text()='Булки']").click()

WebDriverWait(driver, 3)
time.sleep(2)
element = driver.find_element(By.XPATH, "./html/body/div/div/main/section[1]/div[2]/h2[1]")

assert 'Булки' in element.text

driver.quit()

