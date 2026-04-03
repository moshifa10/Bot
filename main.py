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
while True:
    # current_time = time.time()
    # elapsed = current_time - start_time
    for i in range(10):
        click_.click()
    # print("Running...")
    element = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    # if elapsed >= 50:
    #     print("5 seconds reached. Stopping program.")
    #     break
# click_.click()