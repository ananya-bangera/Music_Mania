
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from pprint import pprint

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="4c1e708e3d43402eadd803110514915a",
#                                                client_secret="0a32618bfd5c4a7490d8a98a1c05e924",
#                                                redirect_uri="http://127.0.0.1:5000/",
#                                                scope="user-library-read"))



# shows tracks for the given artist

# usage: python tracks.py [artist name]

# from spotipy.oauth2 import SpotifyClientCredentials
# import spotipy
# import sys
# shows tracks for the given artist

# usage: python tracks.py [artist name]



sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])





# client_credentials_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# if len(sys.argv) > 1:
#     artist_name = ' '.join(sys.argv[1:])
#     results = sp.search(q=artist_name, limit=20)
#     for i, t in enumerate(results['tracks']['items']):
#         print(' ', i, t['name'])



# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])


# if len(sys.argv) > 1:
#     search_str = sys.argv[1]
# else:
#     search_str = 'Radiohead'

# sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# result = sp.search(search_str)
# pprint.pprint(result)


# sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

# response = sp.new_releases()

# while response:
#     albums = response['albums']
#     for i, item in enumerate(albums['items']):
#         print(albums['offset'] + i, item['name'])

#     if albums['next']:
#         response = sp.next(albums)
#     else:
#         response = None



# sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# pl_id = 'spotify:playlist:5RIbzhG2QqdkaP24iXLnZX'
# offset = 0

# while True:
#     response = sp.playlist_items(pl_id,
#                                  offset=offset,
#                                  fields='items.track.id,total',
#                                  additional_types=['track'])
    
#     if len(response['items']) == 0:
#         break
    
#     pprint(response['items'])
#     offset = offset + len(response['items'])
#     print(offset, "/", response['total'])

