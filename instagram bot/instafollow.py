import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class InstaFollower:
    def __init__(self, path):
        self.service = Service(path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://www.instagram.com/")


    def login(self, username, Pass):
        time.sleep(3)
        cookie = self.driver.find_element(By.CLASS_NAME, "_a9--._a9_0")
        cookie.click()
        time.sleep(3)
        Username = self.driver.find_elements(By.CLASS_NAME, "_aa4b._add6._ac4d")
        print(Username)
        Username[0].send_keys(username)
        Username[1].send_keys(Pass)
        login = self.driver.find_element(By.CLASS_NAME, "_acan._acap._acas._aj1-")
        login.click()
    def find_followers(self):
        time.sleep(4)
        search = self.driver.find_element(By.CLASS_NAME,"x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd")
        search.click()
        time.sleep(1)
        notnoe = self.driver.find_element(By.CLASS_NAME, "_a9--._a9_1")
        notnoe.click()
        time.sleep(2)
        new_search = self.driver.find_element(By.CLASS_NAME,"x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd")
        new_search.click()
        time.sleep(2)
        new_search = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a")
        new_search.click()
        time.sleep(10)
        # followers = self.driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div')
        followers = self.driver.find_elements(By.CLASS_NAME, "x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        # followers.text
        for i in followers:
            print(i.text)

        # slider = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]')
        # # "x78zum5.x1q0g3np.xl56j7k.xh8yej3.xyinxu5"
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)", slider)
        # # "window.scrollTo(0, document.body.scrollHeight)")
        # print("hello")
        time.sleep(100)
        pass

    # findfollowers
    # follow
