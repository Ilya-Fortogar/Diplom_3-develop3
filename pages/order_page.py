import allure
from pages.base_page import BasePage
from locators.order_list_page_locators import OrderListPageLocators


class OrderPage(BasePage):
    @allure.step('Нажать на заказ')
    def click_order(self):
        self.wait_element(OrderListPageLocators.ORDER)
        self.click_on_element(OrderListPageLocators.ORDER)


    @allure.step('Отображение модального окна с деталями заказа')
    def order_modal_is_displayed(self):
       return self.element_is_displayed(OrderListPageLocators.ORDER_MODAL)


    @allure.step('Количество заказов за все время')
    def get_count_all_orders(self):
        self.wait_element(OrderListPageLocators.ALL_ORDERS_COUNT)
        return self.get_text(OrderListPageLocators.ALL_ORDERS_COUNT)


    @allure.step('Количество заказов за сегодня')
    def get_count_today_orders(self):
        self.wait_element(OrderListPageLocators.TODAY_ORDERS_COUNT)
        return self.get_text(OrderListPageLocators.TODAY_ORDERS_COUNT)


    @allure.step('Получить номер заказа В работе')
    def get_order_in_work(self):
        self.wait_element(OrderListPageLocators.ORDER_IN_WORK)
        return self.get_text(OrderListPageLocators.ORDER_IN_WORK)


    @allure.step('Получить номер последнего заказа')
    def get_last_order_number(self):
        self.wait_element(OrderListPageLocators.LAST_ORDER)
        return self.get_text(OrderListPageLocators.LAST_ORDER)

