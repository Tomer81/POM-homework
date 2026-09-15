#from pycparser.c_ast import Return
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Products(BasePage):

    BACKPACK_TITLE = (By.CSS_SELECTOR, "#item_4_title_link")
    BACK_LIGHT_TITLE = (By.CSS_SELECTOR, "#item_0_title_link")
    BOLT_SHIRT_TITLE = (By.CSS_SELECTOR, "#item_1_title_link")
    FLEECE_JACKET_TITLE = (By.CSS_SELECTOR, "#item_5_title_link")
    ONESIE_TITLE = (By.CSS_SELECTOR, "#item_2_title_link")
    RED_SHIRT_TITLE = (By.CSS_SELECTOR, "#item_3_title_link")
    #ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart")
    ADD_TO_CART_BTN = (By.XPATH, "//button[text()='Add to cart']")
    BACK_BTN = (By.CSS_SELECTOR, "#back-to-products")
    TITLE_PRODUCTS = (By.CSS_SELECTOR, "[data-test='title']")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")

    def __init__(self, driver):
        super().__init__(driver)

    def choose_product(self, option):
        match option:
            case 1:
                self.click(self.BACKPACK_TITLE)
            case 2:
                self.click(self.BACK_LIGHT_TITLE)
            case 3:
                self.click(self.BOLT_SHIRT_TITLE)
            case 4:
                self.click(self.FLEECE_JACKET_TITLE)
            case 5:
                self.click(self.ONESIE_TITLE)
            case 6:
                self.click(self.RED_SHIRT_TITLE)
            case _:
                print("choose nothing")
        self.wait_for_element(self.BACK_BTN)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def back(self):
        self.click(self.BACK_BTN)
        self.wait_for_visibility(self.TITLE_PRODUCTS)

    def get_title_products(self):
        return self.get_text(self.TITLE_PRODUCTS)

    def get_cart_badge(self):
        return self.get_text(self.SHOPPING_CART_BADGE)