from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
 
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
 
sleep(1)
# Clicking a button
'''
button = driver.find_element(By.ID, "registerBtn")
button.click()
sleep(2)
'''
 
# Typing into a text field
text_field = driver.find_element(By.ID, "firstName")
text_field.send_keys("Marko")
sleep(1)
 
# Clearing a text field
'''
text_field = driver.find_element(By.ID, "firstName")
text_field.clear()
sleep(2)
'''
 
text_field = driver.find_element(By.ID, "lastName")
text_field.send_keys("Caric")
# Extracting text from an element
text = text_field.text
print("Extracted Text:", text)
sleep(1)
 
 
# Sending special keys (e.g., Enter key)
#text_field.send_keys(Keys.ENTER)
#sleep(2)
 
text_field = driver.find_element(By.ID, "phone")
text_field.send_keys("111777956768")
sleep(1)

dropdown = Select(driver.find_element(By.ID, "countries_dropdown_menu"))
dropdown.select_by_visible_text("Spain")
sleep(1)
 
text_field = driver.find_element(By.ID, "emailAddress")
text_field.send_keys("marko.caric")
sleep(1)
 
text_field = driver.find_element(By.ID, "password")
text_field.send_keys("Marko1234")
sleep(1)
 
 
# Sending special keys (e.g., Enter key)
#text_field.send_keys(Keys.ENTER)
#sleep(2)

#driver.find_element(By.XPATH,
    #'//*[@id="exampleCheck1"]/label').click()
driver.find_element(By.XPATH,".//*[contains(text(), 'I agree with the terms and conditions')]").click()
sleep(2)
 
 
button = driver.find_element(By.ID, "registerBtn")
button.click()
sleep(2)
 
 
# Close the browser
driver.quit()