from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs']//a[@class='btn btn-default']")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_NAME_ADD_BASKET = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='row']//p[@class='price_color']")
    PRODUCT_PRICE_ADD_BASKET = (By.XPATH, "//div[@id='messages']/div[3]//strong")

class CartPageLocators(object):
    EMPTY_CART = (By.XPATH, "//div[@class='basket-items']//div[@class='row']")
    EMPTY_CART_MESSAGE = (By.XPATH, "//div[@class='page_inner']//div[@id='content_inner']/p")
