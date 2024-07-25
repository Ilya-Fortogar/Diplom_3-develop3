from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON = [By.XPATH, './/*[@href = "/account"]'] #кнопка Личный кабинет в хедере
    CONSTRUCTOR_BUTTON = [By.XPATH, './/p[text() = "Конструктор"]'] #Кнопка Конструктор
    ORDER_LIST_BUTTON = [By.XPATH, './/p[text() = "Лента Заказов"]']  # Кнопка Лента заказов
    ORDER_BUTTON = [By.XPATH, './/button[text() = "Оформить заказ"]'] #Кнопка Оформить заказ
    PACK_BURGER = [By.XPATH, './/h1[text() = "Соберите бургер"]'] #Заголовок Соберите бургер
    INGREDIENT_BUTTON = [By.XPATH, './/p[text() = "Флюоресцентная булка R2-D3"]'] #Булка Флюоресцентная булка
    INGREDIENT_MODAL_WINDOW = [By.XPATH, './/h2[text() = "Детали ингредиента"]'] #Модальное окно Детали ингредиента
    INGREDIENT_MODAL_CLOSE = [By.XPATH, './/button[contains(@class, "modal__close")]'] #Кнопка закрыть модальное окно
    INGREDIENT_COUNT = [By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]'] #Счетчик ингредиента
    BASKET = [By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]'] #Корзина
    ORDER_ID = [By.XPATH, './/p[text() = "идентификатор заказа"]'] #Идентификатор заказа"
    ORDER_NUMBER = [By.XPATH, './/h2[contains(@class, "Modal_modal__title_shadow__3ikwq")]'] #Номер заказа
    OVERLAY = [By.CSS_SELECTOR, '.Modal_modal__loading__3534A']

