import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class demoFindElementID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        # Find element by ID
        #driver.find_element(By.ID, 'login-input').send_keys('test@gmail.com')
        driver.find_element(By.NAME, 'login-input').send_keys('sujon@gmail.com')
        time.sleep(10)


findbyid = demoFindElementID()
findbyid.locate_by_id_demo()
