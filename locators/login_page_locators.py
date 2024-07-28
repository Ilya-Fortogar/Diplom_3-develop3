from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = [By.XPATH, './/label[text() = "Email"]/following-sibling::input']  # Поле ввода Email
    INPUT_PASSWORD = [By.XPATH, './/label[text() = "Пароль"]/following-sibling::input']  # Поле ввода Пароль
    LOGIN_BUTTON = [By.XPATH, './/button[text() = "Войти"]']  # Кнопка "Войти" на странице входа
    RECOVER_PASSWORD_BUTTON = [By.XPATH, './/a[text() = "Восстановить пароль"]'] #Кнопка Восстановить пароль