import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class OrderPageScooter(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ждём загрузки главной страницы сайта')
    def wait_for_load_home_page(self):
        self.wait_for_element(HomePageLocators.PANEL_HOME_FIRST_PART)

    def click_button(self, locator):
        self.find_element(*locator).click()

    def enter_text(self, locator, text):
        self.find_element(*locator).send_keys(text)

    @allure.step('Ждём загрузки элемента')
    def wait_for_load_element(self, locator):
        self.wait_for_element(locator)

    @allure.step('Скроллим до нужного элемента')
    def scroll_to_element(self, locator):
        self.scroll_into_view(*locator)

    @allure.step("Проверка отображения подтверждения успешного заказа")
    def successful_order_is_displayed(self, locator):
        return self.panel_confirm_order_is_displayed(locator)
