import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
username = "aditya._.6969"
Pass = "wbgs7ffuller"
chrome_driver_path = "/Users/adityabhagavatula/chromedriver-mac-x64/chromedriver"
from instafollow import InstaFollower
bot = InstaFollower(chrome_driver_path)
bot.login(username, Pass)
bot.find_followers()