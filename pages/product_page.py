from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        #product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        #basket_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADD_BASKET).text
        #product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        #basket_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADD_BASKET).text
        #assert product_price == basket_product_price, "Basket price is not correct"
        #assert product_name == basket_product_name, "Basket product name is not correct"
