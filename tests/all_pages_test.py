from selenium import webdriver
from pages.complete_page import CompletePage
from pages.overview_page import OverviewPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.products_page import Products
from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.saucedemo.com/")

p1 = LoginPage(driver)
p1.fill_info("standard_user", "secret_sauce")
p1.login()

p2 = Products(driver)
p2.wait_for_visibility(p2.TITLE_PRODUCTS)
p2.choose_product(3)
p2.add_to_cart()
p2.back()
p2.wait_for_visibility(p2.TITLE_PRODUCTS)
p2.choose_product(5)
p2.add_to_cart()
p2.back()
p2.shopping_cart()
WebDriverWait(driver, 10).until(EC.url_contains("cart.html"))
p3 = CartPage(driver)
p3.checkout()

WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one.html"))

p4 = CheckoutPage(driver)
p4.fill_info("Tomer", "Darmon", "34403")
p4.continue_click()

WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-two.html"))
p5 = OverviewPage(driver)
p5.wait_for_visibility(p5.OVERVIEW_TITLE)
p5.finish()

WebDriverWait(driver, 10).until(EC.url_contains("checkout-complete.html"))
p6 = CompletePage(driver)
print(p6.get_title_text())

input("end")

