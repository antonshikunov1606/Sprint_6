import allure
import pytest
from selenium import webdriver

from tests.test_data import URLCollection
from pages.home_page import HomePageLocators
from pages.home_page import HomePageScooter


@allure.step('Открываем браузер Firefox')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 820)
    yield driver
    driver.quit()


@allure.step('Открываем главную страницу Scooter')
@pytest.fixture
def open_home_page(driver):
    driver.get(URLCollection.SCOOTER_HOME_PAGE)


@pytest.fixture
def open_home_page_and_click_order_buttons(driver, location):
    home_page = HomePageScooter(driver)
    driver.get(URLCollection.SCOOTER_HOME_PAGE)
    home_page.wait_for_load_home_page()
    if location == 'top':
        home_page.click_button(HomePageLocators.BUTTON_ORDER_ON_HEADER)
    elif location == 'bottom':
        home_page.scroll_down_to_button_order()
        home_page.wait_for_load_element(HomePageLocators.BUTTON_ORDER_ON_BOTTOM)
        home_page.click_button(HomePageLocators.BUTTON_ORDER_ON_BOTTOM)


@pytest.fixture
def open_home_page_and_click_order(driver):
    home_page = HomePageScooter(driver)
    driver.get(URLCollection.SCOOTER_HOME_PAGE)
    home_page.wait_for_load_home_page()
    home_page.click_button(HomePageLocators.BUTTON_ORDER_ON_HEADER)
