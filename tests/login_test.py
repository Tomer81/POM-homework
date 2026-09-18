from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import Products

#test login 1- test_valid_username_password
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

p1 = LoginPage(driver)
p1.fill_info("standard_user", "secret_sauce")
p1.login()

products_page = Products(driver)
if "Products" in products_page.get_title_products():
    print("test 1 pass- valid username and password")
else:
    print("test 1 failed - failed")

driver.quit()

#test login 2- test_missing_username
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

p1 = LoginPage(driver)
p1.fill_info("", "secret_sauce")
p1.login()

missing_username = p1.bring_text()
if "Username is required" in missing_username:
    print("test 2 passed- ERROR MSG display")
else:
    print("test 2 failed- ERROR MSG display")
driver.quit()

#test login 3 - test_missing_password
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

p1 = LoginPage(driver)
p1.fill_info("standard_user", "")
p1.login()

missing_password = p1.bring_text()
if "Password is required" in missing_password:
    print("test 3 passed- ERROR MSG display")
else:
    print("test 3 failed- ERROR MSG display")
driver.quit()



