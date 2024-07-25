import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "/Users/adityabhagavatula/chromedriver-mac-x64/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
# number= driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # number.click()
# search = driver.find_element(By.CLASS_NAME,"cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only search-toggle")
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# time.sleep(5)
driver.get("http://secure-retreat-92358.herokuapp.com/")
time.sleep(1)
f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("omolola")
f_name.send_keys(Keys.ENTER)

l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("mcdowall")
f_name.send_keys(Keys.ENTER)

email = driver.find_element(By.NAME, "email")
email.send_keys("mcdowall@ghfdjsk.com")
button = driver.find_element(By.XPATH, "/html/body/form/button")
button.click()
time.sleep(5)