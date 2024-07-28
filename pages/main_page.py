import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Url


class MainPage(BasePage):
    @allure.step('Открыть главную страницу Stellar Burgers')
    def open_main_page(self):
        self.open_page(Url.STELLAR_BURGERS)


    @allure.step('Дождаться и нажать на кнопку Личный кабинет')
    def wait_and_click_account_button(self):
        self.wait_until_element_clickable(MainPageLocators.ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.ACCOUNT_BUTTON)


    @allure.step('Клик на кнопку Конструктор')
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)


    @allure.step('Клик на кнопку Лента заказов')
    def click_order_list_button(self):
        self.wait_element(MainPageLocators.ORDER_LIST_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_LIST_BUTTON)


    @allure.step('Клик на кнопку Оформить заказ')
    def click_order_button(self):
        self.wait_element(MainPageLocators.ORDER_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_BUTTON)


    @allure.step('Клик на кнопку Личный кабинет')
    def click_account_button(self):
        self.click_problem_element(MainPageLocators.ACCOUNT_BUTTON)


    @allure.step('Клик на ингредиент')
    def click_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT_BUTTON)


    @allure.step('Закрыть модальное окно')
    def click_modal_close(self):
        self.wait_element(MainPageLocators.INGREDIENT_MODAL_CLOSE)
        self.click_on_element(MainPageLocators.INGREDIENT_MODAL_CLOSE)


    @allure.step('Отображение модального окна с номером заказа')
    def id_modal_is_displayed(self):
        self.wait_until_element_clickable(MainPageLocators.INGREDIENT_MODAL_CLOSE)
        self.wait_element(MainPageLocators.ORDER_ID)
        return self.element_is_displayed(MainPageLocators.ORDER_ID)


    @allure.step('Получить название модального окна')
    def modal_text(self):
        return self.get_text(MainPageLocators.INGREDIENT_MODAL_WINDOW)


    @allure.step('Отображение Соберите бургер')
    def wait_visibility_constructor_header(self):
        self.wait_element(MainPageLocators.PACK_BURGER)
        return self.get_text(MainPageLocators.PACK_BURGER)


    @allure.step('Перетащить ингредиент в корзину')
    def ingredient_drag_and_drop(self):
        self.wait_element(MainPageLocators.INGREDIENT_BUTTON)
        self.drag_and_drop(MainPageLocators.INGREDIENT_BUTTON, MainPageLocators.BASKET)


    @allure.step('Получить количество булок в корзине')
    def get_count_bun(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNT)


    @allure.step('Получить номер заказа')
    def get_order_number(self):
        self.wait_invisibility(MainPageLocators.OVERLAY)
        return self.get_text(MainPageLocators.ORDER_NUMBER)

