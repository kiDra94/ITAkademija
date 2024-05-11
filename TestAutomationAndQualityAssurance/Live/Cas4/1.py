from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
from time import sleep


usr = input('Enter Email ID: ')
pwd = getpass('Enter Password: ') #sakriva password


driver = webdriver.Edge()
driver.get('https://github.com/login')

print(driver.title) # Sign in to GitHub · GitHub
# print(driver.page_source)


username_box = driver.find_element(By.ID, 'login_field')
username_box.send_keys(usr)
print('Username entered')
sleep(2)

password_box = driver.find_element(By.NAME, 'password')
password_box.send_keys(pwd)
print('Password entered')
sleep(2)

subbmint_btn = driver.find_element(By.NAME, 'commit')
subbmint_btn.click()
print('Form is submited.')
sleep(2)


link = driver.find_element(By.LINK_TEXT, 'kiDra94/seleniumTest')
link.click()
print('Clicked on link.')
sleep(2)


code_btn = driver.find_element(By.ID, ':R55ab:')
code_btn.click()
print('Clicked on button.')
sleep(2)


link = driver.find_element(By.LINK_TEXT, 'Download ZIP')
link.click()
print('File downloaded')
sleep(2)


driver.quit()
print('Finished')