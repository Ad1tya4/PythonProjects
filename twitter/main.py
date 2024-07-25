TWITTER_U = "Aditya06038459"
TWITTER_P = "wbgs7ffuller"
UP = 100
down = 400
chrome_driver_path = "/Users/adityabhagavatula/chromedriver-mac-x64/chromedriver"
from internetspeedbot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot(chrome_driver_path)
# data = bot.get_speeds()
# print(data)
twit = bot.tweet(TWITTER_U)