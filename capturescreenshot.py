
import time

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class DemoScreenShot():
    def demo_screenshot_capture(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        continuedemo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continuedemo.screenshot("./Screenshots/test.png")
        continuedemo.click()
        time.sleep(2)
        
        driver.get_screenshot_as_file("C:\\Users\\RajuAhmed\\Desktop\\Automation Selenium Python")
        driver.save_screenshot("./Screenshots/test1.png")
        


ddscreenshot= DemoScreenShot()
ddscreenshot.demo_screenshot_capture()




