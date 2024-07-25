import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "/Users/adityabhagavatula/chromedriver-mac-x64/chromedriver"
class Formhandler:
    def __init__(self, url):
        self.service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(url)
    def do_stuff(self):
        time.sleep(1)
        inputs = self.driver.find_elements(By.CSS_SELECTOR,".whsOnd.zHQkBf")
        for i in inputs:
            i.send_keys("hello")
        but = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/div[2]")
        time.sleep(100)
        but.click()
        time.sleep(100)