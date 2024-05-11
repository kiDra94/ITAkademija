import random
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import string
 
 
class PythonOrgSearch(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Edge()

    def randomword(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))
 
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title) # gleda da li je rijec u driver.title
        elem = driver.find_element(By.NAME, "q") # izbor elementa - tekst polje za pretragu
        lista_reci  = ['pycon','python','text']
        #elem.send_keys("pycon") # unos teksta za pretragu
        #for i in ['pycon','python','text']:
        for _ in range(10):
            elem = driver.find_element(By.NAME, "q")
            elem.clear()
            #elem.send_keys(i)
            elem.send_keys(self.randomword(10))
            sleep(3)
            elem.send_keys(Keys.RETURN) # kliktanje dugmeta RETURN
            #self.assertNotIn("No results found.", driver.page_source) # provera da li ima rezultata
 
    def tearDown(self):
        self.driver.close()
 
 
if __name__ == "__main__":
    unittest.main()