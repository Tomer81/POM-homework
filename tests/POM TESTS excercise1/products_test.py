from selenium import webdriver
from pages.products_page import Products
from pages.login_page import LoginPage
from helpers.shortcuts import login_shortcut

#test 1-products
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

product_numbers = p2.get_cart_badge()
if product_numbers == "2":
    print("test 1 passed - correct matching amount of products numbers")
else:
    print("test 1 failed - different amount of products numbers")

driver.quit()

#test 2- products
driver = login_shortcut()
p2 = Products(driver)
p2.choose_product(1)
p2.add_to_cart()
p2.back()
p2.choose_product(2)
p2.add_to_cart()
p2.back()
p2.choose_product(3)
p2.add_to_cart()
p2.back()
p2.choose_product(4)
p2.add_to_cart()
p2.back()
p2.choose_product(5)
p2.add_to_cart()
p2.back()
p2.choose_product(6)
p2.add_to_cart()
p2.back()
product_numbers = p2.get_cart_badge()
if product_numbers == "6":
    print("test 2 passed - correct matching amount of products numbers")
else:
    print("test 2 failed - different amount of products numbers")

driver.quit()
