import allure
import pytest

from pages.home_page_yandex import HomePageYandex
from pages.order_page import OrderPageScooter
from pages.home_page import HomePageScooter
from test_data import order_data


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
    def test_make_an_order(self, driver, open_home_page, first_name, second_name, address,
                           metro_station, metro_selection, phone_number, delivery_date, date_selection,
                           rental_period, scooter_color, courier_comment, location):
        order_page = OrderPageScooter(driver)
        home_page = HomePageScooter(driver)
        if location == 'top':
            home_page.click_button_order_on_header()
        elif location == 'bottom':
            home_page.scroll_down_to_button_order()
            home_page.wait_for_load_down_button_order()
            home_page.click_button_order_bottom()
        order_page.enter_first_name(first_name)
        order_page.enter_second_name(second_name)
        order_page.enter_address(address)
        order_page.enter_metro_station(metro_station)
        order_page.wait_for_element(metro_selection)
        order_page.choose_metro_station(metro_selection)
        order_page.enter_phone_number(phone_number)
        order_page.click_button_next()
        order_page.enter_delivery_date(delivery_date)
        order_page.select_delivery_date(date_selection)
        order_page.click_to_select_rental_period()
        order_page.choose_rental_period(rental_period)
        order_page.choose_scooter_color(scooter_color)
        order_page.enter_comment_for_courier(courier_comment)
        order_page.click_make_an_order()
        order_page.wait_for_load_confirmation_order()
        order_page.click_button_yes_to_confirm_order()
        order_page.wait_for_load_successful_order()
        assert order_page.successful_order_is_displayed() is True, \
            'Окно  с сообщением об успешном создании заказа не отобразилось.'


class TestLogoNavigation:
    @allure.title('Проверка перехода на главную страницу "Самоката" при нажатии на логотип "Самокат"')
    def test_clicking_scooter_logo_navigates_to_home_page(self, driver, open_order_page):
        order_page = OrderPageScooter(driver)
        order_page.click_button_logo_scooter()
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page()
        actual_result = order_page.get_current_url()
        expected_result = 'https://qa-scooter.praktikum-services.ru/'

        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'

    @allure.title('Проверка перехода на главную страницу "Дзена" при нажатии на логотип Яндекса')
    def test_clicking_yandex_logo_navigates_to_yandex_home_page(self, driver, open_order_page):
        order_page = OrderPageScooter(driver)
        order_page.click_button_logo_yandex()
        home_page_yandex = HomePageYandex(driver)
        home_page_yandex.switch_to_new_window()
        home_page_yandex.wait_for_load_home_page()
        actual_result = home_page_yandex.get_current_url()
        expected_result = 'https://dzen.ru/?yredirect=true'
        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'
