import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DemoDragDrop():
    def drag_drop(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        elem1 = driver.find_element(By.ID, "draggable")
        elem2 = driver.find_element(By.ID, "droppable")
        #ActionChains(driver).drag_and_drop_by_offset(elem1,elem2).perform()
        ActionChains(driver).drag_and_drop_by_offset(elem1, 452, 88).perform()
        time.sleep(10)

dd = DemoDragDrop()
dd.drag_drop()
