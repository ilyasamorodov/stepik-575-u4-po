from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_promo_link()
        self.has_add_to_basket_button()
        self.has_product_title()
        self.has_product_price()

    
    def should_be_product_promo_link(self):
        assert self.is_current_url_valid(ProductPageLocators.PRODUCT_PROMO_LINK), "Not a product promo page!"


    def has_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is missing!"


    def has_product_title(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), "Product title is missing!"


    def has_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is missing!"


    def success_message_contains_product_title(self):
        assert self.get_success_message_text() == self.get_product_title(), "No product title in success add to basket message"

    def has_no_success_message(self):
        return self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_TEXT)


    def has_disappeared_success_message(self):
        return self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_TEXT)


    def get_success_message_text(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_TEXT).text


    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text


    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text


    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
