from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CompletePage(BasePage):

    BACK_HOME_BTN = (By.CSS_SELECTOR, "#back-to-products")
    PDF_ORDER_BTN = (By.CSS_SELECTOR, "#generate-pdf-order")
    TITLE_TXT = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def __init__(self, driver):
            super(). __init__(driver)

    def back_home(self):
        self.click(self.BACK_HOME_BTN)

    def generate_pdf(self):
        self.click(self.PDF_ORDER_BTN)

    def get_title_text(self):
        return self.get_text(self.TITLE_TXT)