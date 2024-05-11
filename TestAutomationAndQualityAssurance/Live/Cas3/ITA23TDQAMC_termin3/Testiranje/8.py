from selenium import webdriver
from time import sleep
 
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
sleep(2)
 
# Close the browser
driver.quit()
 