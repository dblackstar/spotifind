import spotipy
import spotipy.util as util

class UserCredentials:
    def __init__(self):
        self.scope = 'user-library-read'
        self.client_id = "YOUR CLIENT ID HERE"
        self.client_secret = "YOUR CLIENT SECRET HERE"
        self.redirect_uri = "http://localhost:8888/callback"

    @property
    def get_token(self):
        return util.prompt_for_user_token(
            scope = self.scope,
            client_id = self.client_id,
            client_secret = self.client_secret,
            redirect_uri = self.redirect_uri
        )
