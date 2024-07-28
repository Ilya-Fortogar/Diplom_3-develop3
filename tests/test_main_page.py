import allure
from conftest import driver
from data import Data, Url, Ingridients


class TestMainPage:
    @allure.title('Переход по клику на Конструктор')
    def test_constructor_button(self, main_page):
        main_page.open_main_page()
        main_page.click_account_button()
        main_page.click_constructor_button()
        assert main_page.get_current_url() == Url.STELLAR_BURGERS


    @allure.title('Переход по клику на Лента заказов')
    def test_order_list_button(self, main_page):
        main_page.open_main_page()
        main_page.click_order_list_button()
        assert main_page.get_current_url() == Url.ORDER_LIST_PAGE


    @allure.title('Клик на ингредиент открывает окно с деталями')
    def test_ingredient_modal_open(self, main_page):
        main_page.open_main_page()
        main_page.click_ingredient()
        assert main_page.modal_text() == Ingridients.INGRIDIENT_INFO_1


    @allure.title('Клик на крестик закрывает окно с деталями')
    def test_ingredient_modal_close(self, main_page):
        main_page.open_main_page()
        main_page.click_ingredient()
        main_page.click_modal_close()
        assert main_page.wait_visibility_constructor_header() == Ingridients.FOOD_TASK_1


    @allure.title('При добавлении ингредиента счетчик этого ингредиента увеличивается')
    def test_ingredient_count(self, main_page):
        main_page.open_main_page()
        main_page.ingredient_drag_and_drop()
        assert main_page.get_count_bun() == Ingridients.BURGER_COUNT


    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_make_order_auth_user(self, main_page,login_page):
        main_page.open_main_page()
        main_page.wait_and_click_account_button()
        login_page.login_account(Data.data)
        main_page.ingredient_drag_and_drop()
        main_page.click_order_button()
        assert main_page.id_modal_is_displayed() == True

