import time

from selenium import webdriver
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
time.sleep(1)
p2.add_to_cart()
p2.wait_for_cart_count(1)
time.sleep(1)
p2.back()
p2.choose_product(5)
p2.add_to_cart()
p2.wait_for_cart_count(2)
#p2.back()
p2.shopping_cart()

input("END")
