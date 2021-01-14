from spotipy.oauth2 import SpotifyClientCredentials
from credentials import UserCredentials
from urllib.request import urlopen
from urllib import request as rq
from spotipy import Spotify
from youtube_dl import YoutubeDL
from pathlib import Path
import requests
import eyed3
import re


userCredentials = UserCredentials()

class SongInfo:

    def __init__(self, title, artist, album, cover):
        self.title = title
        self.artist = artist
        self.album = album
        self.cover = cover


class SpotifyTracks:

    def __init__(self):
        self.spotify = Spotify(auth=userCredentials.get_token)

    def get_songs_data(self, results):
        songs = []
        
        for item in results['items']:
            track = item['track'] if 'track' in item else item
            album = track['album']['name']
            artist = track['artists'][0]['name']
            title = track['name']
            cover = track['album']['images'][0]['url']
            songs.append(SongInfo(title, artist, album, cover))
        return songs

    def get_playlist(self, playlist_id, username=userCredentials.client_id):
        saved_songs = []
        results = self.spotify.user_playlist_tracks(username,playlist_id)
        partial_results = self.get_songs_data(results)
        saved_songs += partial_results
        tracks = results['items']
        try:
            while True:
                    results = self.spotify.next(results)
                    tracks.extend(results['items'])
                    partial_results = self.get_songs_data(results)
                    saved_songs += partial_results

                    if not results['next']:
                        break
        except Exception:
            pass 

        return saved_songs

    def get_saved_songs(self, limit=10000):
        offset = 0
        saved_songs = []

        while offset < limit:
            results = self.spotify.current_user_saved_tracks(
                limit=50, offset=offset)
            partial_results = self.get_songs_data(results)

            if not partial_results:
                break

            saved_songs += partial_results
            offset += 50
        return saved_songs[:limit]

class Downloader:

    def get_ydl_opts(self, path):
        return {
            "format": "bestaudio/best",
            "outtmpl": f"{path}/%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
        }    
        
    def add_tags(self, song_path, song):
        cover = urlopen(song.cover).read()
        audiofile = eyed3.load(song_path)
        tag = audiofile.tag
        tag.artist = song.artist
        tag.title = song.title
        tag.album = song.album
        tag.images.set(3, cover, 'cover/jpeg')
        tag.save(version=eyed3.id3.ID3_V2_3)

    def download_yt_song(self, name, path, song):
        name = '+'.join(name.split()).encode('utf-8')
        try:
            with YoutubeDL(self.get_ydl_opts(path)) as ydl:
                html = rq.urlopen(
                    f"https://www.youtube.com/results?search_query={name}"
                )
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

                if video_ids:
                    url = "https://www.youtube.com/watch?v=" + video_ids[0]
                    info = ydl.extract_info(url, download=True)
                    songname = info.get('title', None)
                    dest = (path +'\\'+songname+'.mp3')
                    self.add_tags(dest, song)
        except Exception:
            pass

    def spotify_download(self, path, songs, limit):
        print("\nPress 'Ctrl+C' if you want to stop.")

        for i, song in enumerate(songs[:limit], 1):
            print(f"\nSong {i} of {limit}.", end="")
            name = f'{song.artist} {song.title}'
            print(f"\nDownloading: {song.title} - {song.artist}")  
            self.download_yt_song(name, path, song)
