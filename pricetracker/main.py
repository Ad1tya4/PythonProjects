import requests
from bs4 import BeautifulSoup
import smtplib
url = "https://www.amazon.co.uk/Sportsroyals-Station-Strength-Training-Equipment/dp/B07SM8VJ6P/ref=sr_1_2_sspa?crid=1PYUUMNU94QZ6&keywords=pull+up+bar&qid=1692031630&s=sports&sprefix=pull+up+bar%2Csports%2C76&sr=1-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
}
responce = requests.get(url=url, headers=headers)
webpage = responce.text
soup = BeautifulSoup(webpage, "html.parser")
price = soup.find(class_ = "aok-offscreen")
print(price)
price = price.getText()
price = price.split()[0]
price = price.split("£")
price = float(price[1])
if price < 140:
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login("awsome.adit@gmail.com","ppngccjmmbrenizw")
        conn.sendmail(
            from_addr="awsome.adit@gmail",
            to_addrs="aditya.bhagavatula04@gmail.com",
            msg=f"Subject:ITS CHEAPPP!\n\nits bare cheap {price}:{url}"
        )