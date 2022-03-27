import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
import time

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'


@pytest.fixture
def browser():
    print('browser for tests')
    browser = webdriver.Chrome()
    yield browser
    print('quit browser')
    browser.quit()


class Test():

    def get_link(self, browser):
        browser.get(link)

        button = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
        button.click()

    # def solve_quiz_and_get_code(self, browser):
    #     alert = browser.switch_to.alert
    #     x = alert.text.split(" ")[2]
    #     answer = str(math.log(abs((12 * math.sin(float(x))))))
    #     alert.send_keys(answer)
    #     time.sleep(1)
    #     alert.accept()
    #     try:
    #         alert = browser.switch_to.alert
    #         alert_text = alert.text
    #         print(f"Your code: {alert_text}")
    #         alert.accept()
    #     except NoAlertPresentException:
    #         print("No second alert presented")
