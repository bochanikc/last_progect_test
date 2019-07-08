from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_NAME_ADD_BASKET = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='row']//p[@class='price_color']")
    PRODUCT_PRICE_ADD_BASKET = (By.XPATH, "//div[@id='messages']/div[3]//strong")
