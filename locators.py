from selenium.webdriver.common.by import By
class Locators:
    REG_LOC = (By.CLASS_NAME, 'Auth_link__1fOlj') # Сcылка на Зарегистрироваться со страницы /login
    NAME = (By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']") # Имя на странице /register
    EMAIL = (By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']") # Email на странице /register
    PASS = (By.XPATH, ".//div[@class='input__container']//input[@name='Пароль']") # Пароль на странице /register
    REGISTRATION_BUTTON = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Зарегистрироваться']") # Кнопка Зарегистрироваться на странице /register
    ENTRANCE_BUTTON = (By.XPATH, ".//h2[text()='Вход']") # Копка Вход на странице  /login
    EMAIL_FIELD = (By.XPATH, ".//div[@class='input__container']//input[@name='name']") # Поле емэйл на странице /login
    PASS_FIELD = (By.XPATH, "//div[@class='input__container']//input[@name='Пароль']") # Поле пароль на странице /login
    ENTER_BUTTON = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//button[text()='Войти']") # Кнопка Войти на странице /login
    VISIBLE_COMPONENT_ON_MAIN = (By.XPATH, "//main[@class='App_componentContainer__2JC2W']//h1[@class='text text_type_main-large mb-5 mt-10']") # Компонент, до к-рого ожидаем загрузку на главной странице
    LICHNIJ_KABINET = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']//p[text()='Личный Кабинет']") # Вход в личный кабинет
    LINK_VOSSTAN_PASS = (By.XPATH, ".//p[2]/a[text()='Восстановить пароль']") # Ссылка на Восстановить пароль на странице /login
    VOSSTAN_PASS = (By.XPATH, ".//main[@class='App_componentContainer__2JC2W']//h2[text()='Восстановление пароля']") # Локатор для страницы с восстановлеием пароля
    VOSSTANOVIT_PASS = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Восстановить']") # Кнопка Восстановить пароль на странице /forgot-password
    VVEDITE_KOD_IZ_PISMA= (By.XPATH, ".//div[@class='input__container']//label[text()='Введите код из письма']") # Кнопка Введите код из письма на странице /forgot-password
    VVEDITE_NOVIJ_PASS = (By.XPATH, ".//div[@class='input__container']//input[@name='Введите новый пароль']") # Кнопка Введите новый пароль на странице /reset-password
    SOHRANIT = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Сохранить']") # Кнопка Сохранить на странице /reset-password
    KNOPKA_VOITI = (By.XPATH, ".//p/a[text()='Войти']") # Кнопка Войти на странице /reset-password
    LICHN_KABINET = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']//p[text()='Личный Кабинет']") # Личный кабинет
    SOHRANIT_V_LICHN_KAB= (By.XPATH, ".//div[@class='Profile_profile__3dzvr']//button[text()='Сохранить']") # Компонент, ло которого ожидается загрузка ЛК, кнопка Сохранить
    KONSTRUCTOR = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']//p[text()='Конструктор']") # Кнопка Конструктор
    KNOPKA_STELLAR_BURGERS = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # Кнопка Stellar Burgers
    KNOPKA_EXIT = (By.XPATH, ".//ul[@class='Account_list__3KQQf mb-20']//button[text()='Выход']") # Кнопка Выход из личного кабинета
    NACHINKI = (By.XPATH, ".//span[text()='Начинки']") # Таб Начинки
    EL_TWO = (By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']") # Новый класс при нажатии таба
    NACHINKI_EL_ONE = (By.XPATH, ".//span[text()='Начинки']/parent::div") # Начинки первый элемент
    SOUSI = (By.XPATH, ".//span[text()='Соусы']")  # Таб Соусы
    SOUSI_EL_ONE = (By.XPATH, ".//span[text()='Соусы']/parent::div")  # Соусы первый элемент
    BULKI = (By.XPATH, ".//span[text()='Булки']")  # Таб Булки
    BULKI_EL_ONE = (By.XPATH, ".//span[text()='Булки']/parent::div")  # Булки первый элемент
