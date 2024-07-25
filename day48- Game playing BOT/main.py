import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "/Users/adityabhagavatula/chromedriver-mac-x64/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
# time.sleep(20)
# driver is j a device driver so it allows selenium webdriver to communicate with our chosen browser \
# seleneum provides the script/enables us to use the webpage but it communicates w the webdriver
# of our chosen browser which then communicates w the browser itself it acts as a layer of abstration
# # as the selenium doesnt need to knowe the intracices of how the browser works it communicates w the driver
# and the driver handles it for that specific browser cus each browser is different and each device has
# hardwaere( cpu) shich has its own specifc machiene language/code which is hardwired so the driver is
# specific to that version of the browser on that type of machiene so it knows and can handle the commands
# specifically for that computer. impossible for selenium to handeke the commands for all comouters where
# they have all different machiene code which is hard wired and different browsers".shrubbery time"
timedat = driver.find_elements(By.CSS_SELECTOR,".event-widget.last .shrubbery time" )
times = [(i.get_attribute("datetime")).split("T")[0] for i in timedat]# time = timedat.get_attribute("datetime")

print(times)
date = driver.find_elements(By.CSS_SELECTOR,".event-widget.last .shrubbery .menu a")
dates = [i.text for i in date]
print(dates)
# date = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
# dates = [i.text for i in date]
# print(dates)
dict = {}

for i in range(0,len(times)):
    dict[i] ={
        "time":times[i],
        "name":dates[i]
    }
        # dict[times[i]]=dates[i]
print(dict)