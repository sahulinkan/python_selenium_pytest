## CSS selecotrs combinations practice

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_driver=webdriver.Chrome()
chrome_driver.maximize_window()

chrome_driver.get("https://www.facebook.com")

## css selector : tag and id 
                # --> tagname#id input#email
                
chrome_driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("linkan")
time.sleep(1)
print(chrome_driver.find_element(By.CSS_SELECTOR,"input#email").get_attribute("value"))

## css selector : tag and class 
                # --> tagname.classvalue input.inputtext

chrome_driver.find_element(By.CSS_SELECTOR,"input.inputtext").clear()            
chrome_driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("sahulinkan7")
print(chrome_driver.find_element(By.CSS_SELECTOR,"input.inputtext").get_attribute("value"))

## css selector : tag and attribute
                # --> tagname[attribute=value] input[data-testid='royal-email']
chrome_driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal-email']").clear()             
chrome_driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal-email']").send_keys("linkan kumar sahu")
print(chrome_driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal-email']").get_attribute("value"))

## css selector : only attribute without tag name
                # --> [attribute=value] input[data-testid='royal-email']
chrome_driver.find_element(By.CSS_SELECTOR,"[data-testid='royal-email']").clear()
chrome_driver.find_element(By.CSS_SELECTOR,"[data-testid='royal-email']").send_keys("test css selector")
print(chrome_driver.find_element(By.CSS_SELECTOR,"[data-testid='royal-email']").get_attribute("value"))

## css selector : tag class and attribute
                # --> tagname.class[attribute=value]
                
chrome_driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid='royal-email']").clear()
chrome_driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid='royal-email']").send_keys("Deepak")
chrome_driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid='royal-pass']").send_keys("mypass")
print(chrome_driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid='royal-email']").get_attribute("value"))
print(chrome_driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid='royal-pass']").get_attribute("value"))