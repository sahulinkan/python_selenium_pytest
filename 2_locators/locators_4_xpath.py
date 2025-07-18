from selenium import webdriver
from selenium.webdriver.common.by import By

## XPATHS  :   mostly used in automation with selenium 

chrome_driver=webdriver.Chrome()
chrome_driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(chrome_driver.find_element(By.XPATH,"").text)
