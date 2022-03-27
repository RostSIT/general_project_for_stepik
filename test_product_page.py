from .pages.main_page import MainPage
from .pages.product_page import PageObject
import time


def test_guest_can_see_page(browser):
    # link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    page = MainPage(browser, link)
    page.open()
    time.sleep(1)
    page.guest_should_something()
    button = PageObject(browser, browser.current_url)
    button.guest_should_something()
    time.sleep(1)
