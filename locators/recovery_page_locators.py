from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    RECOVERY_BUTTON = [By.XPATH, './/button[text() = "Восстановить"]'] #Кнопка Восстановить
    SAVE_BUTTON = [By.XPATH, './/button[text() = "Сохранить"]']  #Кнопка Сохранить
    EYE_BUTTON = [By.XPATH, './/div[contains(@class, "icon-action")]'] #Кнопка переключения видимости пароля
    RECOVERY_HEADER = [By.XPATH, './/h2[text() = "Восстановление пароля"]'] #Заголовок Восстановление пароля
    FOCUSED_INPUT_PASSWORD = [By.XPATH, './/*[contains(@class,"input__placeholder")]']  #Поле ввода Пароль