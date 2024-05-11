from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
 
# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
 
# Navigate to the website
driver.get("https://qa-practice.netlify.app/bugs-form.html")
 
# Validate the title
expected_title = "Bug Report Form"
actual_title = driver.title
print(actual_title)
 
if expected_title == actual_title:
    print("Title validation successful!")
else:
    print("Title validation failed. Expected:”, expected_title, “Actual:", actual_title)
 
# Sending keys to an input field
text_field = driver.find_element(By.ID, "firstName")
text_field.send_keys("Hello, World!") # upis teksta
sleep(2)
# Combining keys (e.g., Ctrl+A to select all text)
text_field.send_keys(Keys.CONTROL + "a") # selektovanje teksta
 
 
# Performing double click action
sleep(2)
element = driver.find_element(By.ID, "registerBtn")
actions = ActionChains(driver)
actions.double_click(element).perform()
sleep(2)
# Close the browser