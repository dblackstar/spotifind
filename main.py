from pathlib import Path
from spotifind import SpotifyTracks, Downloader
import sys
import os


if __name__ == "__main__":

    spotify_tracks = SpotifyTracks()
    downloader = Downloader()

    os.system('cls')
    print("Type [1] to download your liked songs")
    print("Type [2] to download songs from a playlist")
    print("Type [3] to exit the program")
    choise = int(input(">"))

    if choise == 1:
        songs = spotify_tracks.get_saved_songs()
        num_songs = (len(songs))
        print(f"\nYou have {num_songs} liked songs.")

    elif choise == 2:
        print("\nEnter the playlist ID")
        playlist_id = input(">")
        songs = spotify_tracks.get_playlist(playlist_id)   

        if not songs:
             print("\nWrong playlist ID or the playlist is empty")
             sys.exit()

        num_songs = len(songs)
        print(f"\nThere are {num_songs} songs in this playlist.")
            
    elif choise == 3:
        sys.exit()

    else:
        print("\nPlease choose a valid option")  
        sys.exit() 

    print("\nChoose where to download your songs")
    print("Type [1] to name and create a folder here")
    print("Type [2] to enter a custom path")
    print("Type [3] to exit the program")
    choise = int(input(">"))

    if choise == 1:
        print("\nEnter the name of the folder")
        folder = input(">")
        
        if not os.path.exists(folder):
            os.mkdir(folder)
        path = os.path.basename(folder)        

    elif choise == 2:
        print("\nEnter the path where you want your songs")
        route = input(">")
        
        if not os.path.exists(route):
            print("\nInvalid path")
            sys.exit()
        
        os.chdir(Path(route))
        path = route   

    elif choise == 3:
        sys.exit()

    else:
        print("\nPlease choose a valid option")  
        sys.exit()     

    downloader.spotify_download(path, songs, limit=num_songs)
