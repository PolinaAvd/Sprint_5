# https://stellarburgers.nomoreparties.site/register

By.XPATH, "./html/body/div/div/main/div/form/fieldset[1]/div/div/input" # User
By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input" # email
By.XPATH, "//div[@class='input__container']//input[@name='Пароль']" # Пароль 
By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Зарегистрироваться']" # Зарегистрироваться

# https://stellarburgers.nomoreparties.site/login

By.XPATH, ".//div[@class='input__container']//input[@name='name']" # email
By.XPATH, ".//div[@class='input__container']//input[@name='Пароль']" # Пароль
By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Войти']" # Войти

# 'https://stellarburgers.nomoreparties.site/forgot-password'

By.XPATH, ".//div[@class='input__container']//input[@name='name']" # email
By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Восстановить']" # Восстановить

# 'https://stellarburgers.nomoreparties.site/reset-password'

By.XPATH, "//div[@class='input__container']//input[@name='Введите новый пароль']" # Пароль 
By.XPATH, "//div[@class='input__container']//input[@name='name']" # Код 
By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Сохранить']" # Сохранить
By.XPATH, "//html/body/div/div/main/div/div/p/a" # Войти

# 'https://stellarburgers.nomoreparties.site/'

By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']//p[text()='Личный Кабинет']" # Личный кабинет
By.XPATH, ".//div[@style='display: flex;']//span[text()='Булки']" # Булки
By.XPATH, ".//div[@style='display: flex;']//span[text()='Соусы']" # Соусы
By.XPATH, ".//div[@style='display: flex;']//span[text()='Начинки']" # Начинки

# 'https://stellarburgers.nomoreparties.site/account/profile'

By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']//p[text()='Конструктор']" # Переход в конструктор по кнопке Конструктор
By.XPATH, "./html/body/div/div/header/nav/div/a" # Переход в конструктор по кнопке Stellar burgers
By.XPATH, ".//ul[@class='Account_list__3KQQf mb-20']//button[text()='Выход']" # Выход