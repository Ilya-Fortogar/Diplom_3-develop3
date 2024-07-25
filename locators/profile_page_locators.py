from selenium.webdriver.common.by import By


class ProfilePageLocators:
    HISTORY_BUTTON = [By.XPATH, './/a[text() = "История заказов"]'] #Кнопка История заказов
    LOGOUT_BUTTON = [By.XPATH, './/button[text() = "Выход"]'] #Кнопка Выход
    ORDER_HISTORY = [By.XPATH, './/div[contains(@class, "OrderHistory_textBox__3lgbs")]/p[contains(@class, "text text_type_digits-default")])[last()]'] #История заказов пользователя

