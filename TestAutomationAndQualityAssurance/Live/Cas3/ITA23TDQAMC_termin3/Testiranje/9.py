from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
 
# Create a new instance of the Chrome driver
from selenium.webdriver.support.select import Select
 
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
 
sleep(3)
# Clicking a button
button = driver.find_element(By.ID, "registerBtn")
button.click()
sleep(3)
# Clicking a link
link = driver.find_element(By.LINK_TEXT, "Dropdowns")
link.click()
sleep(3)
 
# Clicking a button
# Selecting an option by visible text
dropdown = Select(driver.find_element(By.ID, "dropdown-menu"))
dropdown.select_by_visible_text("Brazil")
sleep(2)
 
# Clicking a button
# Selecting an option by visible text
dropdown = driver.find_element(By.ID, "multi-level-dropdown-btn")
dropdown.click()
sleep(2)