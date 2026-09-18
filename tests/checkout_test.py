import time
from selenium import webdriver
from helpers.shortcuts import checkout_shortcut
from pages.overview_page import  OverviewPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.products_page import Products
from pages.login_page import LoginPage

#test1 valid information inside the fields
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

p1 = LoginPage(driver)
p1.fill_info("standard_user", "secret_sauce")
p1.login()

p2 = Products(driver)
p2.wait_for_visibility(p2.TITLE_PRODUCTS)
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
overview_title = p5.overview_txt()
if overview_title == "Checkout: Overview":
    print("test1- passed- valid information has been checked out successfully")
else:
    print("test1-failed- invalid information has been checked out successfully")

driver.quit()

#test2-empty postal code field
driver = checkout_shortcut()
p4 = CheckoutPage(driver)
p4.fill_info("Tomer", "Darmon", "")
p4.continue_click()

postal_msg = p4.error_info_msg()
if postal_msg == "Error: Postal Code is required":
    print("test2-passed - postal code error msg has been shown after empty field")
else:
    print("test2-failed - was able to continue the next page")

driver.quit()

#test3 - empty first name field
driver = checkout_shortcut()
p4 = CheckoutPage(driver)
p4.fill_info("", "Darmon", "1989")
p4.continue_click()
first_name = p4.error_info_msg()
if first_name == "Error: First Name is required":
    print("test3-passed - first name error msg has been shown after empty field")
else:
    print("test3-failed - was able to continue the next page")

driver.quit()

#test4 - empty last name field
driver = checkout_shortcut()
p4 = CheckoutPage(driver)
p4.fill_info("Tomer", "", "1989")
p4.continue_click()
last_name = p4.error_info_msg()
if last_name == "Error: Last Name is required":
    print("test4-passed - last name error msg has been shown after empty field")
else:
    print("test4-failed - was able to continue the next page")
driver.quit()

#test5 - empty fields
driver = checkout_shortcut()
p4 = CheckoutPage(driver)
p4.fill_info("", "", "")
p4.continue_click()
error_msg = p4.error_info_msg()
if error_msg == "Error: First Name is required":
    print("test5-passed - error msg has been shown after all empty fields")
else:
    print("test5-failed - was able to continue the next page")
driver.quit()
