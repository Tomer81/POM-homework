from selenium import webdriver
from pages.overview_page import OverviewPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.products_page import Products
from pages.login_page import LoginPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

p1 = LoginPage(driver)
p1.fill_info("standard_user", "secret_sauce")
p1.login()

p2 = Products(driver)
p2.choose_product(3)
p2.add_to_cart()
p2.back()
p2.choose_product(5)
p2.add_to_cart()
p2.back()
p2.shopping_cart()

p3 = CartPage(driver)
p3.checkout()

p4 = CheckoutPage(driver)
p4.fill_info("Tomer", "Darmon", "34403")
p4.continue_click()

p5 = OverviewPage(driver)
p5.finish()

input("end")