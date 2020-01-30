from .base_page import BasePage
from locators import ProductPageLocators


class ProductPage(BasePage):
    
    def should_be_product_promo_link(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PROMO_LINK), "Login link is not presented"


    def has_add_to_basket_button(self):
        pass


    def add_to_basket(self):
        pass
