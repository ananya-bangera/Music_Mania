
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

# if len(saudioys.argv) > 1:
#     search_str = sys.argv[1]
# else:
search_str = 'Atif Aslam'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search(search_str,limit =50)
# print(result)
info_songs= list()
d1 = dict()
for res in result['tracks']['items']:
    print(res['name'])  #track name
    print(res['album']['images'][0]['url'])  #track image
    print(res['preview_url'])    #track url
    d1['name']=res['name']
    d1['artist'] ="Atif Aslam"
    d1['img']=res['album']['images'][0]['url']
    d1['src']=res['preview_url']
    info_songs.append(d1)
# print(info_songs)
# print(sp.featured_playlists(locale=None, country="IN", timestamp=None, limit=20, offset=0))
print(sp.artist('spotify:artist:4YRxDV8wJFPHPTeXepOstw')['images'][0]['url'])
# print(info_songs)
# return info_songs
# for res in result:
#     pprint.pprint(res)