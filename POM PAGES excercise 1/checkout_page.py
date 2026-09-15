from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#continue")
    CHECKOUT_INFO = (By.CSS_SELECTOR, "[data-test='title']")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")
    #LAST_NAME_ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")
    #FIRST_NAME_ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")



    def __init__(self, driver):
        super().__init__(driver)

    def fill_info(self, name, last_name, postal_code):
        self.fill_text(self.FIRST_NAME, name)
        self.fill_text(self.LAST_NAME, last_name)
        self.fill_text(self.POSTAL_CODE, postal_code)


    def continue_click(self):
        self.click(self.CONTINUE_BTN)

    def checkout_text(self):
        return self.get_text(self.CHECKOUT_INFO)

    def error_info_msg(self):
        return self.get_text(self.ERROR_MSG)

    #def last_name_error(self):
        return self.get_text(self.LAST_NAME_ERROR_MSG)

   # def first_name_error(self):
        return self.get_text(self.FIRST_NAME_ERROR_MSG)