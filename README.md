<h1>spotifind</h1>
<p>Download songs from your Spotify playlists and liked songs using youtubedl</p>
<br>
<p>First of all, you need to create an app in spotify for developers</p>
 https://developer.spotify.com/dashboard/applications
<br>
<p>once created, you need to copy your Client ID and Client secret</p>
<img src="imgs/settings.PNG">
<br>
<p>and then in the same page, go to settings and change the redirect URI to "http://localhost:8888/callback "</p>
<img src="imgs/uri.PNG">
<br>
<p>Once you have your ID and Secret, go to credentials.py and copy/paste them where asked, and you are good to go, just call main.py</p>
<br>
<p>To download a playlist, you need its ID, just go to your playlist, go to 'Share' in the 3 dots menu, and copy the link.</p>
<p>The ID is the string of characters after the last dash.</p>
<img src="imgs/link.PNG">