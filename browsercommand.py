import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class BrowserCommand():
    def demo_browser(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.gozayaan.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.minimize_window()
        driver.fullscreen_window()
        driver.refresh()
        clickable = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
        clickable.click()
        time.sleep(4)  # you can see the input
        driver.back()
        time.sleep(4)  # you can see the input
        driver.forward()
        time.sleep(4)  # you can see the input
        driver.minimize_window()
        time.sleep(4)  # you can see the input
        driver.quit()

hellobrowser = BrowserCommand()
hellobrowser.demo_browser()