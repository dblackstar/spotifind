# spotifind
Download songs from your Spotify playlists and liked songs using youtubedl
<br>
First of all, you need to mkae an app in spotify for developers
 https://developer.spotify.com/dashboard/applications
<br>
once created, you need to copy your Client ID and Client secret
<img>
<br>
and then in the same page, go to settings and change the redirect URI to "http://localhost:8888/callback "
<img>
<br>
Once you have your ID and Secret, go to credentials.py and copy/paste them where asked, and you are good to go, just call main.py
<br>
To download a playlist, you need its ID, just go to your playlist, go to 'Share' in the 3 dots menu, and copy the link.
The ID is the string of chracter after the last dash.
<img>
