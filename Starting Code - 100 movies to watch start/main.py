import requests

from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")
titles = soup.find_all(name="h3", class_ = "title")
names = [title.getText() for title in titles[::-1]]
names = "\n".join(names)


with open("movies.txt", mode="a") as file:
    file.writelines(names)