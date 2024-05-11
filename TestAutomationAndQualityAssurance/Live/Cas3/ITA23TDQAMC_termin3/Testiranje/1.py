from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
 
#driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("http://www.python.org")
print(driver.title)
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
sleep(10)
elem.clear()
sleep(5)
elem.send_keys("pycon") # unos reči u  tekstualno polje za pretragu
sleep(5)
elem.send_keys(Keys.RETURN) # stiskanje tastera enter
sleep(5)
print(driver.page_source)
assert "No results found." not in driver.page_source
driver.close()