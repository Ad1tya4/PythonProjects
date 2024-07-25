import os
import requests

tok = os.environ.get("TOKEN")
sheety = os.environ.get("SHEETY_URL")
kiwi_API = os.environ.get("KIWI_API")
teq_auth = {"apikey":kiwi_API}
cities = []
tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"
auth ={"Authorization":"Bearer fewifewBFBVMNSFKJ"}
responce = requests.get(url=f"{sheety}", headers=auth)
data = responce.json()["prices"]
print(data)
for i in data:
    cities.append(i["city"])
print(cities)
for i in cities:
    query = {
        "term":i,
        "location_types":"city"

    }
    responce2 = requests.get(url=tequila_endpoint, headers=teq_auth, params=query)

    code=(responce2.json()["locations"][0]["code"])
    prices = {
        "price": {
            "IATA Code":code
        }
    }
    responce3 = requests.put(url =sheety, json=prices, headers=auth)
    print(responce3.status_code)