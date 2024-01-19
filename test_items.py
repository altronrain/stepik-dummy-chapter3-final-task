import time
from selenium.webdriver.common.by import By

class TestStepik3_6_5():
    
    def test_add_to_basket_btn(self, browser):
        # No language is set here
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(30)
        add_to_basket_btn = browser.find_elements(
            By.CLASS_NAME, 'btn-add-to-basket'
            )
        assert add_to_basket_btn, 'Button is not there!'
        """
        Seems like on Chrome v.120.+ this site use en-gb by default when
        non-supported locale received. That means assert has no effect. 
        Instead we could add button text print. But this contradicts the task.
        """
        # print(f'\nButton text is: {add_to_basket_btn[0].text}')