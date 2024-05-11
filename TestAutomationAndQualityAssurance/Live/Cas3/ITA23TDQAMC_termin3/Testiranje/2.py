from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
 
url = "https://www.python.org"
driver = webdriver.Edge()
driver.maximize_window()
driver.get(url)
 
print(driver.title)
 
sleep(2)
#id i name su izcitani iz html koda od web stranice
search_bar = driver.find_element(By.ID, "id-search-field")
#search_bar = driver.find_element(By.NAME, "q")
sleep(2)
 
search_bar.clear()
sleep(2)
search_bar.send_keys("getting started with python")
sleep(2)
search_bar.send_keys(Keys.RETURN)
sleep(2)
 
print(driver.current_url)
 
driver.close()