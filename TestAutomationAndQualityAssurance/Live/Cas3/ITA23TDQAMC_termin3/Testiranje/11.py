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
# XPATH ako su elemnti ugnjezdeni, pokazujemo im putanju
driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[2]/td/label').click()
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

# Select tuesday
driver.find_element(By.XPATH,
    '//*[@id="q15"]/table/tbody/tr[3]/td/label').click()
sleep(2)

# Close the browser
driver.quit()
 