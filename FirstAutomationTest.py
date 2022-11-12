from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get('https://chaldal.com/')

print(driver.title)
driver.maximize_window()

driver.close()

# Web driver manager: pip install webdriver-manager
# URL: https://pypi.org/project/webdriver-manager/
"""
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
"""