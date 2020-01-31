from pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize('offer_number', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(offer_number)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_contains_product_title()
    assert page.get_product_price() in page.get_basket_total_price(), "Product and basket prices are not equal!"
