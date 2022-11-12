import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")

        # Find element by ID
        # driver.find_element(By.ID, 'login-input').send_keys('test@test.com')

        # Find element by Link text
        #clickable = driver.find_element(By.LINK_TEXT, "Villas & Stays")
        #PARTIAL Link text
        clickable = driver.find_element(By.PARTIAL_LINK_TEXT, "Holida")
        clickable.click()
        time.sleep(4)  # you can see the input


findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()

