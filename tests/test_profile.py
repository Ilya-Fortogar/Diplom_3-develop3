import allure
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from conftest import driver
from data import Data, Url


class TestProfilePage:
    @allure.title('Переход по клику на Личный Кабинет')
    def test_cross_via_account_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_account_button()
        assert main_page.get_current_url() == Url.LOGIN_PAGE


    @allure.title('Переход в раздел История заказов')
    def test_cross_order_history(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_and_click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Data.data)
        main_page.wait_and_click_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_history_button()
        assert main_page.get_current_url() == Url.HISTORY_ORDER_PAGE


    @allure.title('Выход из аккаунта')
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_and_click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Data.data)
        main_page.wait_and_click_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_logout_button()
        login_page.wait_login_button()
        assert main_page.get_current_url() == Url.LOGIN_PAGE