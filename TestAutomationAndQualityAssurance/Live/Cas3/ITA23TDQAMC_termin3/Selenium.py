from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("http://www.python.org")
print(driver.title)
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon") # unos reči u  tekstualno polje za pretragu
elem.send_keys(Keys.RETURN) # stiskanje tastera enter
print(driver.page_source)
assert "No results found." not in driver.page_source
driver.close()

---------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.python.org"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

print(driver.title)

sleep(3)
#search_bar = driver.find_element(By.ID, "id-search-field")
search_bar = driver.find_element(By.NAME, "q")
sleep(3)

search_bar.clear()
sleep(3)
search_bar.send_keys("getting started with python")
sleep(3)
search_bar.send_keys(Keys.RETURN)
sleep(3)

print(driver.current_url)

driver.close()

---------------------------------------------------------------

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q") # izbor elementa - tekst polje za pretragu
        elem.send_keys("pycon") # unos teksta za pretragu
        elem.send_keys(Keys.RETURN) # kliktanje dugmeta RETURN
        self.assertNotIn("No results found.", driver.page_source) # provera da li ima rezultata

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

	
--------------------------------------------------------------

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

--------------------------------------------------------------

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
sleep(3)

# Find element using element's id attribute
driver.find_element(By.ID, "user-name").send_keys("standard_user")
sleep(3)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
sleep(3)
driver.find_element(By.ID, "login-button").click()
sleep(5)

text = driver.find_element(By.CLASS_NAME, "title").text
print(text)

# Check if login was successful
assert "products" in text.lower()
print("TEST PASSED : LOGIN SUCCESSFUL")

# Close the driver
driver.quit()

--------------------------------------------------------------

# Import selenium module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Using chrome driver
driver = webdriver.Chrome()

# Web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

sleep(2)
# Selecting radio button
# Select male
driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label').click()
sleep(2)
# Selecting check box
# Select sunday
driver.find_element(By.XPATH,
    '//*[@id="q15"]/table/tbody/tr[1]/td/label').click()
sleep(2)
# Select monday
driver.find_element(By.XPATH,
    '//*[@id="q15"]/table/tbody/tr[2]/td/label').click()
sleep(2)
# Close the browser
driver.quit()

--------------------------------------------------------------

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
sleep(3)

# Find element using element's id attribute
driver.find_element(By.ID, "user-name").send_keys("standard_user")
sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
sleep(2)
driver.find_element(By.ID, "login-button").click()
sleep(2)

text = driver.find_element(By.CLASS_NAME, "title").text
print(text)

# Check if login was successful
assert "products" in text.lower()
print("TEST PASSED : LOGIN SUCCESSFUL")


print("testing add to cart")
add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
# Click three buttons to make the cart_value 3
for btns in add_to_cart_btns[:3]: # prva tri dugmeta
    sleep(2)
    btns.click()

cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
assert "3" in cart_value.text
print("TEST PASSED : ADD TO CART", "\n")

# Close the driver
driver.quit()

----------------------------------------------------------------

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
sleep(3)

# Find element using element's id attribute
driver.find_element(By.ID, "user-name").send_keys("standard_user")
sleep(3)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
sleep(3)
driver.find_element(By.ID, "login-button").click()
sleep(3)

text = driver.find_element(By.CLASS_NAME, "title").text
print(text)

# Check if login was successful
assert "products" in text.lower()
print("TEST PASSED : LOGIN SUCCESSFUL")


print("testing add to cart")
add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
# Click three buttons to make the cart_value 3
for btns in add_to_cart_btns[:3]: # prva tri dugmeta
    btns.click()
    sleep(2)

cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
print(cart_value.text)
assert "3" in cart_value.text
print("TEST PASSED : ADD TO CART", "\n")


print("testing remove from cart")
remove_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for btns in remove_btns[:2]:
    btns.click()
    sleep(2)

print(cart_value.text)
assert "1" in cart_value.text
print("TEST PASSED : REMOVE FROM CART", "\n")

# Close the driver
driver.quit()

-----------------------------------------------------------------

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

------------------------------------------------------------------

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

-----------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
# Clicking a button
button = driver.find_element(By.ID, "registerBtn")
button.click()
sleep(2)

# Typing into a text field
text_field = driver.find_element(By.ID, "firstName")
text_field.send_keys("Marko")
sleep(2)

# Clearing a text field
text_field = driver.find_element(By.ID, "firstName")
text_field.clear()
sleep(2)

text_field = driver.find_element(By.ID, "lastName")
text_field.send_keys("Caric")
# Extracting text from an element
text = text_field.text
print("Extracted Text:", text)
sleep(2)


# Sending special keys (e.g., Enter key)
#text_field.send_keys(Keys.ENTER)
#sleep(2)

text_field = driver.find_element(By.ID, "phone")
text_field.send_keys("111777956768")
sleep(2)


text_field = driver.find_element(By.ID, "emailAddress")
text_field.send_keys("marko.caric")
sleep(2)


text_field = driver.find_element(By.ID, "password")
text_field.send_keys("Marko1234")
sleep(2)


# Sending special keys (e.g., Enter key)
#text_field.send_keys(Keys.ENTER)
#sleep(2)


button = driver.find_element(By.ID, "registerBtn")
button.click()
sleep(2)


# Close the browser
driver.quit()

-------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

# Selecting an option by visible text
dropdown = Select(driver.find_element(By.ID, "countries_dropdown_menu"))
dropdown.select_by_visible_text("Bermuda")
sleep(2)
# Selecting an option by value
dropdown.select_by_value("Afganistan")
sleep(2)
# Selecting an option by index
dropdown.select_by_index(7)
sleep(2)
# Close the browser
driver.quit()

---------------------------------------------------------------------

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
driver.quit()

----------------------------------------------------------------------------

