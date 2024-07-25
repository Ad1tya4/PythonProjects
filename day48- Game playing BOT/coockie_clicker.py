import time
# from checker import Checker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "/Users/adityabhagavatula/chromedriver-mac-x64/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
# options = driver.find_elements(By.CSS_SELECTOR, "#store")
# list = options[0].text.splitlines()
# prices =[]
# for i in list[::2]:
#     prices.append(i)
# new = [i.split() for i in prices]
# print(new)
# newer= []
# for i in new:
#     if i[2] == "-":
#         newer.append(i[3])
#     else:
#         newer.append(i[2])
# newer = [int(i.replace(",","")) for i in newer]
# print(newer)
# money = driver.find_element(By.ID, "money")
# money = int(money.text)
# print(money)


five_min = time.time() + 5*60
timeout = time.time()+5
cookie = driver.find_element(By.ID, "cookie")

timeout_start = time.time()

while True:

    cookie.click()
    if time.time() > timeout:
        options = driver.find_elements(By.CSS_SELECTOR, "#store")
        list = options[0].text.splitlines()
        prices = []
        for i in list[::2]:
            prices.append(i)
        new = [i.split() for i in prices]

        newer = []
        names = []
        print(new)
        for i in new:
            if i[2] == "-":
                names.append(f"{i[0]} {i[1]}")
                newer.append(i[3])
            else:
                names.append(i[0])
                newer.append(i[2])
        newer = [int(i.replace(",", "")) for i in newer]
        money = driver.find_element(By.ID, "money")
        money = int(money.text)

        dict = {names[i]:newer[i] for i in range(0,7)}
        counter = -1
        for i in newer:
            if money > i:
                counter += 1
        answer = names[counter]
        print(answer)
        but = driver.find_element(By.ID, f"buy{answer}")
        but.click()


    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID,"cps").text
        print(cookie_per_s)
        break
