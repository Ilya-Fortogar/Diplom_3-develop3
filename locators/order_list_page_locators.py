from selenium.webdriver.common.by import By


class OrderListPageLocators:
    ORDER = [By.XPATH, './/li[contains(@class, "OrderHistory_listItem")]'] #Заказ
    LAST_ORDER = [By.XPATH, '//li[1]//p[@class="text text_type_digits-default"]'] #Последний заказ
    ORDER_MODAL = [By.XPATH, './/div[contains(@class, "Modal_orderBox")]'] #Окно с деталями заказа
    ORDER_IN_WORK = [By.XPATH, './/*[contains(@class, "orderListReady")]//li[contains(@class,"digits-default")]'] #Заказ в работе
    ALL_ORDERS_COUNT = [By.XPATH, './/p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "digits-large")]']  #Счетчик всех заказов
    TODAY_ORDERS_COUNT = [By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "digits-large")]']  #Счетчик заказов за сегодня