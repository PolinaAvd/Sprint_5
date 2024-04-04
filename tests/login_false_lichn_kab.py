from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

driver.find_element(By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']//p[text()='Личный Кабинет']").click()

time.sleep(3)

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()

