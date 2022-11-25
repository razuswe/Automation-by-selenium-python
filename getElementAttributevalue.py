import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class DemoGetAttributeValue():
    def demo_get_value(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        attr_value = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(attr_value)


attrobj = DemoGetAttributeValue()
attrobj.demo_get_value()