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
allMusic= list()
d1 =dict()
for res in result['tracks']['items']:
    d1['name']=res['name']
    d1['artist'] ="Atif Aslam"
    d1['img']=res['album']['images'][0]['url']
    d1['src']=res['preview_url']
    allMusic.append(d1)