import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "/Users/adityabhagavatula/chromedriver-mac-x64/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3700103825&f_AL=true&f_E=2&keywords=python%20developer&refresh=true")
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()
u_name = driver.find_element(By.CSS_SELECTOR, "#username ")
u_name.send_keys("aditya.bhagavatula04@gmail.com")
l_name = driver.find_element(By.CSS_SELECTOR, "#password ")
l_name.send_keys("M@@d789495")
sign_in = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large.from__button--floating")
sign_in.click()
list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for i in list:
    print(i.text)

time.sleep(10000)