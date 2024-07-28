import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.recovery_page_locators import RecoveryPageLocators


class RecoveryPage(BasePage):
    @allure.step('Нажать кнопку Восстановить')
    def click_recovery_button(self):
        self.wait_element(RecoveryPageLocators.RECOVERY_BUTTON)
        self.click_on_element(RecoveryPageLocators.RECOVERY_BUTTON)


    @allure.step('Нажать кнопку видимости пароля')
    def click_eye_button(self):
        self.wait_element(RecoveryPageLocators.EYE_BUTTON)
        self.click_on_element(RecoveryPageLocators.EYE_BUTTON)


    @allure.step('Отображение Восстановление пароля')
    def wait_visibility_recovery_header(self):
        self.wait_element(RecoveryPageLocators.RECOVERY_HEADER)
        return self.get_text(RecoveryPageLocators.RECOVERY_HEADER)


    @allure.step('Дождаться кнопки Сохранить')
    def wait_visibility_save_button(self):
        self.wait_element(RecoveryPageLocators.SAVE_BUTTON)


    @allure.step('Проверить активность поля')
    def check_is_active_field(self):
        return self.text_attribute(RecoveryPageLocators.FOCUSED_INPUT_PASSWORD, 'input__placeholder-focused')

