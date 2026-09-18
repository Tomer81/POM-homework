from selenium import webdriver
from helpers.shortcuts import complete_shortcut
from pages.complete_page import CompletePage
from pages.overview_page import OverviewPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.products_page import Products
from pages.login_page import LoginPage

#test 1 purchasing products and expecting to receive a confirmation msg in the end
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
p5.wait_for_visibility(p5.OVERVIEW_TITLE)
p5.finish()
p6 = CompletePage(driver)
complete_title = p6.get_title_text()
if complete_title == "Thank you for your order!":
    print("test 1 - successfully receiving a confirmation msg after order")
else:
    print("test 1 - failed in receiving a confirmation msg after order")
driver.quit()

#test-2 checking if a confirmation msg received without purchasing any products
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

p1 = LoginPage(driver)
p1.fill_info("standard_user", "secret_sauce")
p1.login()

p2 = Products(driver)
p2.wait_for_visibility(p2.TITLE_PRODUCTS)
p2.shopping_cart()

p3 = CartPage(driver)
p3.checkout()
p4 = CheckoutPage(driver)
p4.fill_info("Tomer", "Darmon", "34403")
p4.continue_click()

p5 = OverviewPage(driver)
p5.wait_for_visibility(p5.OVERVIEW_TITLE)
p5.finish()

driver = complete_shortcut()
p6 = CompletePage(driver)
complete_title = p6.get_title_text()
if complete_title == "Thank you for your order!":
    print("test-2 failed, order confirmation received without selecting any products")
else:
    print("test-2 success, order confirmation received after ordering products")

driver.quit()
