import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class DemoCheckBox():
    def demo_check_box(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")

        # Find element by ID
        # driver.find_element(By.ID, 'login-input').send_keys('test@test.com')
        # demo_state = driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").is_displayed()
        # print(demo_state)

        clickable = driver.find_element(By.ID, "BE_flight_non_stop").is_selected()

        print(clickable)

        time.sleep(4)  # you can see the input


demostate = DemoCheckBox()
demostate.demo_check_box()