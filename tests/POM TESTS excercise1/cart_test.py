import time
from selenium import webdriver

from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.products_page import Products
from pages.login_page import LoginPage
from helpers.shortcuts import login_shortcut

#test 1-cart
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

p1 = LoginPage(driver)
p1.fill_info("standard_user", "secret_sauce")
p1.login()

p2 = Products(driver)
p2.choose_product(3)
time.sleep(3)
p2.add_to_cart()
p2.back()
p2.choose_product(5)
p2.add_to_cart()
p2.back()
p2.shopping_cart()
p3 = CartPage(driver)
time.sleep(2)
p3.checkout()
p4 = CheckoutPage(driver)
checkout_page_info = p4.checkout_text()
if checkout_page_info == "Checkout: Your Information":
    print("test 1- passed")
else:
    print("test 1 - failed")

driver.quit()

#test 2-cart
driver = login_shortcut()
p2 = Products(driver)
p2.choose_product(2)
p2.add_to_cart()
p2.back()
p2.choose_product(3)
p2.add_to_cart()
p2.shopping_cart()
p3 = CartPage(driver)
time.sleep(5)
p3.remove(2)

product_numbers = p2.get_cart_badge()
if product_numbers == "1":
    print("test 1 passed - remove btn is reacting as it should ")
else:
    print("test 1 failed - different amount of products numbers")

driver.quit()


