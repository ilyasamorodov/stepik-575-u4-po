from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def has_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket empty " \
        "message not found!"
    
    def has_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty!"
