import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from dotenv import load_dotenv


# Load API Key hidden in my .env file
# Gather other Spotify Authentification info
load_dotenv()
secret = os.getenv('SPOTIFY_API_KEY')
cid = '8080cfc4325643a78a2096bada866ab2'
redirect_uri = 'http://localhost:8000'
scope = "user-follow-modify user-top-read user-read-recently-played user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-modify-public"


def get_spotify_client():
    """This clears the cached token and returns a spotipy Spotify object

    Returns:
        spotipy.client.Spotify: Spotify API CLient
    """    
    # Clear the cached token (if any)
    if os.path.exists(".cache"):
        os.remove(".cache")

    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= cid, client_secret= secret, redirect_uri= redirect_uri, scope=scope))
    

sp = get_spotify_client()
user_info = sp.current_user()
print(user_info)


def get_user_id():
    """Retrieve the current user ID

    Returns:
        string : spotiy client user ID
    """    
    return sp.current_user()['id']


def get_artist_genre(artist_name):
    """Retrieves the genres associated with an artist

    Args:
        artist_name (string): name of the artist

    Returns:
        list: associated genres
    """    
    try:
        results = sp.search(q='artist:' + artist_name, type='artist') # No request_timeout argument
        items = results['artists']['items']

        if len(items) > 0:
            artist = items[0]
            return artist['genres']
        else:
            return "No genre found for this artist"
    except spotipy.exceptions.SpotifyException as e:
        if e.http_status == 429:
            # Handle rate limiting
            retry_after = int(e.headers['Retry-After'])
            print(f"Rate limit exceeded. Retrying after {retry_after} seconds.")
            time.sleep(retry_after)
            return get_artist_genre(artist_name)
        else:
            print("An error occurred: ", e)
            return "Error"


def get_audio_features_batch(uris):
    """Retrives audio features associated with a song

    Args:
        uris (list): list of song identifiers (uris)

    Returns:
        list: list of dictionaries each containing audio features and their values for each song
    """    
    max_retries = 5
    retry_delay = 5  # start with a 5-second delay

    for attempt in range(max_retries):
        try:
            return sp.audio_features(uris)
        except spotipy.exceptions.SpotifyException as e:
            if e.http_status == 429:
                # Use the Retry-After header to wait the appropriate amount of time
                retry_after = int(e.headers.get('Retry-After', retry_delay))
                print(f"Rate limit exceeded, retrying in {retry_after} seconds...")
                time.sleep(retry_after)
                retry_delay *= 2  # Increase the delay for the next round
            else:
                # Reraise the exception for non-rate-limiting issues
                raise
        except Exception as e:
            # Log other exceptions and break the loop
            print(f"An unexpected error occurred: {e}")
            break

    # If the code reaches this point, it means all retries have been exhausted
    print("Failed to fetch audio features after maximum retries.")
    return None  # or raise an Exception if that's more appropriate for your use case



def get_spotify_uri(track_name, artist_name):
    """Function to search Spotify for a track and return its URI

    Args:
        track_name (string): name of song
        artist_name (string): name of artist

    Returns:
        string: unique identifier (uri) of the of the requested track
    """    
    query = f"track:{track_name} artist:{artist_name}"
    results = sp.search(query, type='track', limit=1)
    items = results['tracks']['items']
    if items:
        # Return the URI of the first result
        return items[0]['uri']
    else:
        # Return None or handle the case where the track is not found
        return None


def user_playlist_create(user_id, playlist_name, playlist_description):
    """Creates a playlist for the current user

    Args:
        user_id (string): ID of the user
        playlist_name (string): name for the playlist to be created
        playlist_description (string): description of the playlist to be created

    Returns:
        None
    """    
    return sp.user_playlist_create(user_id, playlist_name, description=playlist_description)

def user_playlist_add_tracks(user_id, playlist_id, song_uris):
    sp.user_playlist_add_tracks(user_id, playlist_id, song_uris)
    return None