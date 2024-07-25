import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



class InternetSpeedTwitterBot:
    def __init__(self, driverpath):
        self.service = Service(driverpath)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://www.instagram.com/")
    def get_speeds(self):
        self.driver.get("https://www.speedtest.net/result/15164458228")
        try:
            time.sleep(2)
            accept = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            accept.click()
        except NoSuchElementException:
            go_button = self.driver.find_element(By.CSS_SELECTOR,".start-button a")
            go_button.click()
        # else:
        #     go_button = self.driver.find_element(By.CSS_SELECTOR,".start-button a")
        #     go_button.click()
        # while True:
        #     try:
        #         back = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
        #         print("Element is visible? " + str(back.is_displayed()))
        #         self.driver.implicitly_wait(10)
        #         print("Element is visible? " + str(back.is_displayed()))
        #         print(back.text)
        #     except NoSuchElementException:
        #         pass
        #     else:
        #         back.click()
        #         break
        data = self.driver.find_elements(By.CSS_SELECTOR, ".result-data-value")
        data = [float(i.text) for i in data[:2:]]
        return data



        # button = self.driver.find_element(By.CSS_SELECTOR, "#engine-wrapper a")
        # button.click()
    def tweet(self, username):
        self.driver.get("https://twitter.com/messages/1138160410392236033-1372513172121354245")
        time.sleep(2)
        # user = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div')
        # user.send_keys(username)
        # user = self.driver.find_element(By.XPATH, '//*[@id="gsi_208812_902821"]')
        # user.click()
        email = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.click()
        time.sleep(400)
