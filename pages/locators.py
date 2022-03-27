from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class CartLocators:
    BUTTON_LOCATOR = (By.XPATH, '//*[@id="add_to_basket_form"]/button')

    BOOK_ADD = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    BOOK_CART = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')

    PRICE_ADD = (By.CSS_SELECTOR, '.col-sm-6.product_main>p.price_color')
    PRICE_CART = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div strong')
