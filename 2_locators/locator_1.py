from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver=webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.get("http://demo.nopcommerce.com")
chrome_driver.find_element(By.ID,"small-searchterms").send_keys("Shoes")
chrome_driver.find_element(By.CLASS_NAME,"button-1").click()
time.sleep(2)
products=chrome_driver.find_elements(By.CLASS_NAME,"product-title")
for product in products:
    print(product.text)
print(chrome_driver.title)