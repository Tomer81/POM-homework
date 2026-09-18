from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-test='checkout']")
    CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, "#continue-shopping")

    REMOVE_BACKPACK = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    REMOVE_BACK_LIGHT = (By.CSS_SELECTOR, "#remove-sauce-labs-bike-light")
    REMOVE_BOLT_SHIRT = (By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt")
    REMOVE_FLEECE_JACKET = (By.CSS_SELECTOR, "#remove-sauce-labs-fleece-jacket")
    REMOVE_ONESIE = (By.CSS_SELECTOR, "#remove-sauce-labs-onesie")
    REMOVE_RED_SHIRT = (By.CSS_SELECTOR, "#remove-test.allthethings()-t-shirt-(red)")

    def __init__(self, driver):
        super().__init__(driver)

    def checkout(self):
        self.click(self.CHECKOUT_BTN)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def remove(self, option):
        match option:
            case 1:
                self.click(self.REMOVE_BACKPACK)
            case 2:
                self.click(self.REMOVE_BACK_LIGHT)
            case 3:
                self.click(self.REMOVE_BOLT_SHIRT)
            case 4:
                self.click(self.REMOVE_FLEECE_JACKET)
            case 5:
                self.click(self.REMOVE_ONESIE)
            case 6:
                self.click(self.REMOVE_RED_SHIRT)
            case _:
                print("choose nothing")