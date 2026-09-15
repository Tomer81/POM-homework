from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LGN_BTN = (By.CSS_SELECTOR, "#login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def fill_info(self, user_name, password ):
        self.fill_text(self.USER_NAME, user_name)
        self.fill_text(self.PASSWORD, password)

    def login(self):
        self.click(self.LGN_BTN)

    def bring_text(self):
        return self.get_text(self.ERROR_MSG)
