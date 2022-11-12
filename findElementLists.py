import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://yatra.com")

        # Find element by ID
        # driver.find_element(By.ID, 'login-input').send_keys('test@test.com')

        # Find element by Link text
        #clickable = driver.find_element(By.LINK_TEXT, "Holidays")
        #PARTIAL Link text
        #driver.find_element(By.TAG_NAME, "input").send_keys('test@gmail.com')
        lista = driver.find_elements(By.TAG_NAME, "a")
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(5)  # you can see the input


findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()

