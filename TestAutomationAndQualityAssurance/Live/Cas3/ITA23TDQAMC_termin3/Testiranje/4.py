# https://saucelabs.com/resources/blog/selenium-with-python-for-automated-testing
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
 
# Set options for not prompting DevTools information
 
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
 
print("testing started")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
sleep(3)
 
# Get page title
title = driver.title
print(title)
 
 
# Test if title is correct
assert "Swag Labs" in title
print("TEST 0: `title` test passed")
 
 
# Close the driver
driver.quit()