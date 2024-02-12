import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = "Your_Client_ID"
CLIENT_SECRET = "Your_Client_Secret"
REDIRECT_URI = "http://example.com"
SPOTIFY_USER = "Your_User"
scope = "playlist-modify-private"

date = input("What day do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
billboard_website = response.text

# For testing
# song_list = ['Happy', 'All Of Me', 'Dark Horse', 'Talk Dirty', 'Let It Go', 'Pompeii', 'Team', 'Counting Stars', 'The Man', 'Turn Down For What', 'Best Day Of My Life', 'Loyal', 'Timber', 'Not A Bad Thing', 'Show Me', 'Hey Brother', 'Drunk In Love', 'Story Of My Life', 'Say Something', '#SELFIE', 'Let Her Go', 'This Is How We Roll', 'Animals', 'Bottoms Up', 'Wake Me Up!', 'Play It Again', 'Burn', 'Na Na', 'Demons', 'The Monster', 'Royals', 'Human', 'La La La', "Ain't It Fun", 'Partition', 'Drink To That All Night', 'Neon Lights', 'Give Me Back My Hometown', 'Radioactive', "Doin' What She Likes", 'My Hitta', '19 You + Me', 'Paranoid', 'Cop Car', "Can't Remember To Forget You", 'The Worst', 'Classic', 'Get Me Some Of That', 'Roar', 'Rewind', 'Mmm Yeah', 'Do You Want To Build A Snowman?', 'Stoner', 'Goodnight Kiss', 'Trophies', 'Fancy', 'Wild Wild Love', 'Automatic', 'Who Do You Love?', 'She Looks So Perfect', 'Let It Go', 'Beat Of The Music', 'For The First Time In Forever', 'Sleeping With A Friend', 'Me And My Broken Heart', 'Magic', 'I Hold On', 'Stay With Me', 'Move That Doh', 'Man Of The Year', 'When She Says Baby', 'Summer', 'Headlights', "Lettin' The Night Roll", 'Red Lights', 'John Doe', 'Do I Wanna Know?', 'The Walker', 'Empire', 'Take Me Home', 'Up Down (Do This All Day)', 'Invisible', 'Part II (On The Run)', "Beachin'", "Lookin' For That Girl", 'On Top Of The World', 'Whiskey In My Water', 'Helluva Life', 'Adore You', 'Latch', 'Ride', 'Love Is An Open Door', 'Oceans (Where Feet May Fail)', 'Beating Heart', 'Or Nah', 'Slow Me Down', 'Young Girls', 'Come With Me Now', 'Odio', "Everything I Shouldn't Be Thinking About"]

song_list = []
soup = BeautifulSoup(billboard_website, "html.parser")
songs = soup.select("li ul li h3")
for song in songs:
    song_name = song.getText().strip()
    song_list.append(song_name)
print(song_list)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=SPOTIFY_USER))

user_id = sp.current_user()["id"]
song_uris = []
for song in song_list:
    result = sp.search(q=f"Track: {song} year: {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Could not find {song} in Spotify. Skipped.")

playlist_name = f"{date} Billboard Top 100"
playlist = sp.user_playlist_create(user=user_id,
                                   name=playlist_name,
                                   public=False)
sp.playlist_add_items(playlist_id=playlist["id"],
                      items=song_uris)
