import pytest
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def setup(browser):
    # register new user for each test
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    email = str(time.time()) + "@fakemail.org"
    password = email
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.register_new_user(email, password)
    login_page.should_be_authorized_user()


class TestUserAddToBasketFromProductPage():
    def test_user_cant_see_success_message(self, setup, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_product_page()
        assert product_page.has_no_success_message(), "Unexpected success message found!"


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, setup, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.success_message_contains_product_title()
        assert page.get_product_price() in page.get_basket_total_price(), "Product and basket prices are not equal!"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    assert product_page.has_no_success_message(), "Unexpected success message found!"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    assert product_page.has_disappeared_success_message(), "Unexpected success message found!"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.has_no_items()
    basket_page.has_empty_basket_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.success_message_contains_product_title()
