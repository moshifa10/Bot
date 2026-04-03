from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.ChromeOptions()
web.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=web)
driver.get("https://ozh.github.io/cookieclicker/")

# Pause the program for 2 seconds
time.sleep(10)

# button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
# button.send_keys(Keys.ENTER)
click_ = driver.find_element(By.ID, "bigCookie")




start_time = time.time()
enable_crate = False
while True:
    current_time = time.time()
    elapsed = current_time - start_time
    for i in range(10):
        click_.click()
    # print("Running...")
    if elapsed >= 10:
        element = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        crate = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade")

        for i in crate[::-1]:
            crate_string =  i.get_attribute("class")
            crate_classes = crate_string.split()
            if "enabled" in crate_classes:
                i.click()

        for i in element[::-1]:
            class_string = i.get_attribute("class")
            # print(class_string)
            classes =class_string.split()
            if "product" in classes and "unlocked" in classes and "enabled" in classes:
                i.click()
            start_time = time.time()
        
# click_.click()