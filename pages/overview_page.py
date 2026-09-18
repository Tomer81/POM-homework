from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OverviewPage(BasePage):
    FINISH_BTN = (By.CSS_SELECTOR, "#finish")
    CANCEL_BTN = (By.CSS_SELECTOR, "#cancel")
    OVERVIEW_TITLE = (By.CSS_SELECTOR, "[data-test='title']")

    def __init__(self, driver):
        super().__init__(driver)

    def finish(self):
        self.click(self.FINISH_BTN)

    def cancel(self):
        self.click(self.CANCEL_BTN)

    def overview_txt(self):
        return self.get_text(self.OVERVIEW_TITLE)