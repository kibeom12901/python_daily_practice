from bs4 import BeautifulSoup
import requests
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

URL = "https://www.billboard.com/charts/hot-100/"
date_input = input("Enter a date (YYYY-MM-DD) to get the Billboard Hot 100 chart: ")
print(URL + date_input)

response = requests.get(URL + date_input +"/")
response.raise_for_status()
print(response)
data = response.text

soup = BeautifulSoup(data, "lxml")

song_names_spans = soup.select("li ul li h3")
# song_names_spans = soup.find_all(name = "a", class_="c-title__link lrv-a-unstyle-link")
# .strip() to remove \n
song_names = [song.getText().strip() for song in song_names_spans]

print("-------------------\n")
print(song_names)

# Replace with your actual credentials
SPOTIPY_CLIENT_ID = "YOUR_ID"
SPOTIPY_CLIENT_SECRET = "YOUR_SECRET"
SPOTIPY_REDIRECT_URI = "YOUR_URI"  

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))

# Get the authenticated user's ID
user_id = sp.current_user()["id"]
print("-------------------\n")
print(f"Authenticated as: {user_id}")

song_uris = []
year = date_input.split("-")[0] 
print("-------------------\n")
print(year)


for song in song_names:
    query = f"track:{song} year:{year}"  
    results = sp.search(q=query, type="track", limit=1)

    try:
        uri = results["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"⚠️ Song '{song}' not found on Spotify. Skipping...")

print("-------------------\n")
pprint.pp(song_uris)

playlist_name = f"{date_input} Billboard 100"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist["id"]

print(f"✅ Created playlist: {playlist_name} under the id {playlist_id}")

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
print(f"✅ Added {len(song_uris)} songs to '{playlist_name}'.")
