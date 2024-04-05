# Sprint_5

Все тесты в дирректории tests.
Для запуска проекта понадобятся также файл с переменными conftest.py (в дирректории tests), файл с константой URL settings.py и файл c локаторами locators.py.

Проверка регистрации: 
registaryion.py
test_link_to_registaration_successful_registration - успешная регистрация, в этом же же тесте вход через кнопку регистрации
test_link_to_registaration_too_short_pass_fail_registration - ошибка некорректного пароля

Проверка входа: 
login.py
test_successful_enter - вход по кнопке «Войти в аккаунт» на главной
test_not_successful_enter_through_lichn_kab - неуспешный вход для неавторизованного пользователя при нажатии Линый кабинет
test_vosstan_pass_successful - вход через кнопку в форме восстановления пароля

Переход в личный кабинет:
lichnij_kabinet.py
test_perehod_v_lichn_kab_successful_entrance - успешный вход в личный кабинет
test_perehod_iz_lichn_kab_v_konstructor_successful_entrance - переход из ЛК по кнопке Конструктор на главную страницу
test_perehod_iz_lichn_kab_v_konstructor__po_knopke_stellar_burgers_successful_entrance - переход из ЛК по кнопке Stellar burgers на главную страницу

Выход:
exit.py
test_vihod_iz_lichn_kab_successful_exit - успешный выход из ЛК

Переходы булки - соусы - начинки:
bulki_sousi_nachinki.py 
test_tabs_na_glavnoj_stranice_successful_tabbing - поверка нажатия табов 