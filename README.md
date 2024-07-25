# UI tests for Stellar Burgers

## Фикстуры - ***conftest.py***
* `driver` - настройки webdriver

## Набор тестовых данных, список URL - ***data.py***
* `class Data` - валидные данные пользователя
* `class Url` - список URL страниц

## Сценарии, покрытые тестами

### Восстановление пароля - ***test_recovery.py***
* `test_cross_via_recovery_button` - проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"
* `test_set_email_and_click_recovery_button` - проверка ввода почты и клика по кнопке "Восстановить"
* `test_eye_button` - проверка подсвечивания поля Пароль после клика по кнопке показать/скрыть пароль


### Личный кабинет - ***test_profile.py***
* `test_cross_via_account_button` - проверка перехода по клику на "Личный кабинет"
* `test_cross_order_history` - проверка перехода в раздел "История заказов"
* `test_logout` - проверка выхода из аккаунта


### Основной функционал - ***test_main_page.py***
* `test_constructor_button` - проверка перехода по клику на "Конструктор"
* `test_order_list_button` - проверка перехода по клику на "Лента заказов"
* `test_ingredient_modal_open` - проверка отображения всплывающего окна с деталями ингредиента
* `test_ingredient_modal_close` - проверка закрывания всплывающего окна
* `test_ingredient_count` - проверка счетчика количества ингредиентов
* `test_make_order_auth_user` - проверка оформления заказа залогиненным пользователем


### Лента заказов - ***test_order_page.py***
* `test_order_modal_open` - проверка отображения всплывающего окна с деталями заказа
* `test_order_from_history_displayed_order_list` - проверка отображения созданного заказа в "Лента заказов"
* `test_count_orders` - проверка счетчика заказов
* `test_order_in_work` - проверка отображения номера заказа в разделе "В работе"


## Для запуска:
* Установить зависимости
``` shell
pip3 install -r requirements.txt
```
* Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
* Посмотреть отчет
``` shell
allure serve allure_results
```
