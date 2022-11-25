import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class DemoFindElementState():
    def demo_enable_disable(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        demo_state = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(demo_state)

        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        demo_state1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(demo_state1)



attrobj = DemoFindElementState()
attrobj.demo_enable_disable()