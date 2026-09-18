from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    MENU_BTN = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    ALL_ITEMS = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    ABOUT = (By.CSS_SELECTOR, "#about_sidebar_link")
    LOGOUT = (By.CSS_SELECTOR, "#logout_sidebar_link")
    RESET = (By.CSS_SELECTOR, "#reset_sidebar_link")
    CANCEL_BTN = (By.CSS_SELECTOR, "#cancel")
    SHOPPING_CART_BTN = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    TWITTER_BTN = (By.CSS_SELECTOR, ".social_twitter a")
    FACEBOOK_BTN = (By.CSS_SELECTOR, ".social_facebook a")
    LINKDIN_BTN = (By.CSS_SELECTOR, ".social_linkedin a")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def fill_text(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        self.wait_for_element(locator).click()

    def menu(self):
        self.click(self.MENU_BTN)

    def all_items(self):
        self.menu()
        self.click(self.ALL_ITEMS)

    def about(self):
        self.menu()
        self.click(self.ABOUT)

    def logout(self):
        self.menu()
        self.click(self.LOGOUT)

    def reset(self):
        self.menu()
        self.click(self.RESET)

    def cancel(self):
        self.click(self.CANCEL_BTN)

    def shopping_cart(self):
        self.click(self.SHOPPING_CART_BTN)

    def get_text(self, locator):
            return self.wait_for_visibility(locator).text


    def twitter(self):
        self.click(self.TWITTER_BTN)

    def facebook(self):
        self.click(self.FACEBOOK_BTN)

    def linkdin(self):
        self.click(self.LINKDIN_BTN)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def hover(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def select_by_text(self, locator, text):
        element = self.find_element(locator)
        select_object = Select(element)
        select_object.select_by_visible_text(text)
