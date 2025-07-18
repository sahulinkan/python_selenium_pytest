
# Assignment 1
# ===============

# 1) open web browser
# 2) open url https://admin-demo.nopcommerce.com/login
# 3) Provide Email (admin@yourstore.com)
# 4) Provide password (admin)
# 4) click on login
# 5) capture title of the dashboard page (Actual title)
# 6) verify title of the page : "Dashboard / nopCommerce administration" (Expected)

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver=webdriver.Chrome()
chromedriver.maximize_window()
chromedriver.get("https://admin-demo.nopcommerce.com/login")
chromedriver.find_element(By.XPATH,"//input[@type='email']").clear()
chromedriver.find_element(By.XPATH,"//input[@type='email']").send_keys("admin@yourstore.com")
chromedriver.find_element(By.ID,"Password").clear()
chromedriver.find_element(By.ID,"Password").send_keys("admin")

chromedriver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(30)
actual_title= chromedriver.title
print(actual_title)
assert actual_title == "Dashboard / nopCommerce administration"
chromedriver.close()

print("working fine")