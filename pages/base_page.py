from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def find_element(self, locator):
        self.driver.find_element(*locator)


    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()


    def get_text(self, locator):
        return self.driver.find_element(*locator).text


    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)


    def get_current_url(self):
        return self.driver.current_url


    def wait_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))


    def open_page(self, url):
        self.driver.get(url)


    def wait_until_element_clickable(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))


    def click_problem_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(element).click().perform()


    def element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()


    def wait_invisibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))


    def drag_and_drop(self, element, endpoint):
        element = self.driver.find_element(*element)
        endpoint = self.driver.find_element(*endpoint)
        ActionChains(self.driver).drag_and_drop(element, endpoint).perform()


    def text_attribute(self, locator, text):
        return WebDriverWait(self.driver, 20).until(expected_conditions.text_to_be_present_in_element_attribute(locator, 'class', text))

