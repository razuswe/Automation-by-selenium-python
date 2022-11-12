import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        # Find element by ID
        # driver.find_element(By.ID, 'login-input').send_keys('test@test.com')

        # Find element by xpath
        driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys('test@test.com')
        time.sleep(4)  # you can see the input


findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()

