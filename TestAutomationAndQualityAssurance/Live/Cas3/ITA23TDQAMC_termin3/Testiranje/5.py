from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
 
# Set options for not prompting DevTools information
 
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
 
print("testing started")
driver = webdriver.Chrome(options=options)
 
driver.get("https://www.saucedemo.com/")
print(driver.page_source)
sleep(3)
print("----------------------------------")
# Find element using element's id attribute
driver.find_element(By.ID, "user-name").send_keys("standard_user")
sleep(3)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
sleep(3)
driver.find_element(By.ID, "login-button").click()
sleep(5)
 
text = driver.find_element(By.CLASS_NAME, "title").text #
print(text)
 
# Check if login was successful
assert "products" in text.lower()
print("TEST PASSED : LOGIN SUCCESSFUL")
print(driver.page_source)
 
# Close the driver
driver.quit()