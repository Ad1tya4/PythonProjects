import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import SpotifyOAuth
# date = input("What year would you like to travel to? In this format (YYYY-MM-DD)\n")
url = f"https://www.billboard.com/charts/hot-100/2012-07-12/"
client_id ="f1d0f2f909d041a29724a026ab94be22"
client_secret = "a7c4328e035e402880ee21dd66de5342"
spotify= f"https://api.spotify.com/v1/users/{client_id}/playlists"
json = {
    "name": "New Playlist",
    "public": False,
    "collaborative":False,
    "description":"Billboard top 100 #throwback"

}
auth = {
    "user_id":client_id
}
response = requests.get(url)
response.raise_for_status()
website = response.text
soup = BeautifulSoup(website, "html.parser")
data = soup.select("li ul li h3")
data_list = [i.getText().strip() for i in data]
print(data_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="bob",))
current = sp.current_user()
print(current)
# info = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="https://example.com/")
# response = requests.post(url = spotify, json=json, headers=auth)
# response.raise_for_status()