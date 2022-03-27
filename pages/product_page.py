from .base_page import BasePage
from .locators import CartLocators
from .main_page import MainPage
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class PageObject(BasePage):
    def guest_should_something(self):
        self.button_click()
        self.solve_quiz_and_get_code()
        self.test_guest_can_add_product_to_basket()
        self.test_compare_title()
        # self.test_compare_price()

    def button_click(self):
        cart_button = self.browser.find_element(*CartLocators.BUTTON_LOCATOR)
        cart_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        time.sleep(1)
        alert.accept()
        time.sleep(1)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def test_guest_can_add_product_to_basket(self):
        assert self.is_element_present(*CartLocators.BUTTON_LOCATOR), 'Cart button is missing'

    def test_compare_title(self):
        book_add = self.browser.find_element(*CartLocators.BOOK_ADD)
        book_cart = self.browser.find_element(*CartLocators.BOOK_CART)
        # price_add = self.browser.find_element(*CartLocators.PRICE_ADD)
        assert book_add.text == book_cart.text, 'The title of the book in the basket does not match the one added'
        # assert book_add.text == price_add, 'The title of the book in the basket does not match the one added'

    # def test_compare_price(self):
    #
    #     price_add = self.browser.find_element(*CartLocators.PRICE_ADD)
    #     price_cart = self.browser.find_element(*CartLocators.PRICE_CART)
    #
    #     assert price_add.test == price_cart.text, 'The price of the book in the cart does not match the one added'
