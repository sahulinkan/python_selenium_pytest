## find all linksn in the page

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver=webdriver.Chrome()
chrome_driver.get("https://demo.nopcommerce.com/")
links=chrome_driver.find_elements(By.TAG_NAME,"a")
print(len(links))