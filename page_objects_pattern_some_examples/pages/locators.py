from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, '//span/a[text() = "Посмотреть корзину"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    ACCOUNT_LINK = (By.XPATH, "//a[contains (text(), ' Аккаунт')]")


class LoginPageLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[value='Добавить в корзину']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner ")
    BASKET_TEXT = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TEXT = (By.XPATH, "//p[contains (text(), 'Ваша корзина пуста')]")
