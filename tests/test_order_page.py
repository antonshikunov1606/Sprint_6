import allure
import pytest
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPageScooter
from pages.home_page import HomePageScooter
from pages.home_page_yandex import HomePageYandex
from test_data import order_data
from test_data import URLCollection


class TestOrderPage:

    @allure.title('Позитивная проверка заказа самоката с двумя наборами данных')
    @pytest.mark.parametrize(
        'first_name, second_name, address, metro_station, metro_selection, phone_number, delivery_date, date_selection,'
        'rental_period, scooter_color, courier_comment, location',
        [(
                data['first_name'], data['second_name'], data['address'], data['metro_station'],
                data['metro_selection'],
                data['phone_number'], data['delivery_date'], data['date_selection'], data['rental_period'],
                data['scooter_color'], data['courier_comment'], data['location']
        ) for data in order_data]
    )
    def test_make_an_order(self, driver, open_home_page_and_click_order_buttons, first_name, second_name, address,
                           metro_station, metro_selection, phone_number, delivery_date, date_selection,
                           rental_period, scooter_color, courier_comment, location):
        order_page = OrderPageScooter(driver)
        order_page.enter_text(OrderPageLocators.INPUT_FIRST_NAME_FIELD, first_name)
        order_page.enter_text(OrderPageLocators.INPUT_SECOND_NAME_FIELD, second_name)
        order_page.enter_text(OrderPageLocators.INPUT_ADDRESS_FIELD, address)
        order_page.enter_text(OrderPageLocators.INPUT_METRO_STATION_SEARCH, metro_station)
        order_page.wait_for_element(metro_selection)
        order_page.click_button(metro_selection)
        order_page.enter_text(OrderPageLocators.INPUT_PHONE_NUMBER_FIELD, phone_number)
        order_page.click_button(OrderPageLocators.BUTTON_NEXT)
        order_page.enter_text(OrderPageLocators.INPUT_DELIVERY_DATE, delivery_date)
        order_page.click_button(date_selection)
        order_page.click_button(OrderPageLocators.SELECT_RENTAL_PERIOD)
        order_page.click_button(rental_period)
        order_page.click_button(scooter_color)
        order_page.enter_text(OrderPageLocators.INPUT_COMMENT_FOR_COURIER, courier_comment)
        order_page.click_button(OrderPageLocators.BUTTON_MAKE_AN_ORDER)
        order_page.wait_for_load_element(OrderPageLocators.PANEL_CONFIRMATION_TO_ORDER)
        order_page.click_button(OrderPageLocators.BUTTON_YES)
        order_page.wait_for_load_element(OrderPageLocators.PANEL_SUCCESSFUl_ORDER)
        assert order_page.successful_order_is_displayed(OrderPageLocators.PANEL_SUCCESSFUl_ORDER) is True, \
            'Окно  с сообщением об успешном создании заказа не отобразилось.'


class TestLogoNavigation:
    @allure.title('Проверка перехода на главную страницу "Самоката" при нажатии на логотип "Самокат"')
    def test_clicking_scooter_logo_navigates_to_home_page(self, driver, open_home_page_and_click_order):
        order_page = OrderPageScooter(driver)
        order_page.click_button(OrderPageLocators.BUTTON_LOGO_SCOOTER)
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page()
        actual_result = driver.current_url
        expected_result = URLCollection.SCOOTER_HOME_PAGE

        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'

    @allure.title('Проверка перехода на главную страницу "Дзена" при нажатии на логотип Яндекса')
    def test_clicking_yandex_logo_navigates_to_yandex_home_page(self, driver, open_home_page_and_click_order):
        order_page = OrderPageScooter(driver)
        order_page.click_button(OrderPageLocators.BUTTON_LOGO_YANDEX)
        home_page_yandex = HomePageYandex(driver)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[1])
        home_page_yandex.wait_for_load_home_page()
        actual_result = driver.current_url
        expected_result = URLCollection.YANDEX_HOME_PAGE
        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'
