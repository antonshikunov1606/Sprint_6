from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def scroll_into_view(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView()", locator)

    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def send_keys(self, *locator, text=''):
        self.driver.find_element(*locator).send_keys(text)

    def panel_confirm_order_is_displayed(self, locator):
        panel_confirm_order = WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return panel_confirm_order.is_displayed()
