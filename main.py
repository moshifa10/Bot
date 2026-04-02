from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web = webdriver.ChromeOptions()
web.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=web)
driver.get("https://za.indeed.com/l-johannesburg,-gauteng-jobs.html?vjk=89455e1b791bd189")

button = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
button.send_keys("Software Engineering")
click_ = driver.find_element(By.XPATH, '//*[@id="jobsearch"]/div/div[2]/button')
click_.click()