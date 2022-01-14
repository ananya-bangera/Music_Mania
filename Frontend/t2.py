
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
# import sys
# import pprint

# if len(saudioys.argv) > 1:
#     search_str = sys.argv[1]
# else:
# search_str = 'Atif Aslam'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# result = sp.search(search_str,limit =50)
# print(result)
info_songs= list()
# for res in result['tracks']['items']:
    # print(res['name'])  #track name
    # print(res['album']['images'][0]['url'])  #track image
    # print(res['preview_url'])    #track url 
    # info_songs.append([res['name'],res['album']['images'][0]['url'],res['preview_url']])

# print(sp.featured_playlists(locale=None, country="IN", timestamp=None, limit=20, offset=0))
print(sp.artist('spotify:artist:4YRxDV8wJFPHPTeXepOstw')['images'][0]['url'])
# print(info_songs)
# return info_songs
# for res in result:
#     pprint.pprint(res)