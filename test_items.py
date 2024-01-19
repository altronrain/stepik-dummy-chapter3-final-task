import time
from selenium.webdriver.common.by import By

class TestStepik3_6_5():
    
    def test_add_to_basket_btn(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(30)
        add_to_basket_btn = browser.find_elements(
            By.CLASS_NAME, 'btn-add-to-basket'
            )
        assert add_to_basket_btn is not None, 'Button is not there!'
        print(f'\nButton text is: {add_to_basket_btn[0].text}')