import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    @allure.step('Нажать на кнопку История заказов')
    def click_history_button(self):
        self.wait_element(ProfilePageLocators.HISTORY_BUTTON)
        self.click_on_element(ProfilePageLocators.HISTORY_BUTTON)


    @allure.step('Нажать на кнопку Выход')
    def click_logout_button(self):
        self.wait_until_element_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)

