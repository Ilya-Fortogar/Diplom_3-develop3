import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators



class LoginPage(BasePage):
    @allure.step('Ввести почту')
    def set_email(self, email):
        self.send_keys(LoginPageLocators.INPUT_EMAIL, email)


    @allure.step('Ввести пароль')
    def set_password(self, password):
        self.send_keys(LoginPageLocators.INPUT_PASSWORD, password)


    @allure.step('Клик на кнопку Войти')
    def click_login_button(self):
        self.wait_element(LoginPageLocators.LOGIN_BUTTON)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)


    @allure.step('Авторизация')
    def login_account(self, user):
        self.set_email(user['email'])
        self.set_password(user['password'])
        self.click_login_button()


    @allure.step('Дождаться кнопку Войти')
    def wait_login_button(self):
        self.wait_element(LoginPageLocators.LOGIN_BUTTON)


    @allure.step('Нажать на кнопку Восстановить пароль')
    def click_recover_password_button(self):
        self.wait_element(LoginPageLocators.RECOVER_PASSWORD_BUTTON)
        self.click_on_element(LoginPageLocators.RECOVER_PASSWORD_BUTTON)

