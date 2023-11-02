import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup


# Function to scrape the Billboard Hot 100 chart for a given date
def scrape_billboard_chart(date):
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP request errors
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.find_all("span", class_="chart-element__information__song")
    song_names = [song.getText() for song in song_names_spans]
    return song_names


# Function to authenticate with the Spotify API
def authenticate_spotify():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=os.environ["SPOTIPY_CLIENT_ID"],   # Use your client ID
            client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],  # Use your client secret
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    return sp, user_id


# Function to search for songs on Spotify and add them to a playlist
def search_and_add_songs_to_playlist(sp, user_id, date, song_names):
    song_uris = []
    year = date.split("-")[0]

    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        if result["tracks"]["items"]:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        else:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    return playlist


if __name__ == "__main__":
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

    try:
        song_names = scrape_billboard_chart(date)
        sp, user_id = authenticate_spotify()
        playlist = search_and_add_songs_to_playlist(sp, user_id, date, song_names)
        print(f"Playlist created: {playlist['name']}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
