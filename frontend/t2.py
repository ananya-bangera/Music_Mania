
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

# if len(saudioys.argv) > 1:
#     search_str = sys.argv[1]
# else:
# search_str = 'Atif Aslam'

# sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# result = sp.search(search_str,limit =50)
# # print(result)
# info_songs= list()
# d1 = dict()
# for res in result['tracks']['items']:
#     print(res['name'])  #track name
#     print(res['album']['images'][0]['url'])  #track image
#     print(res['preview_url'])    #track url
#     d1['name']=res['name']
#     d1['artist'] ="Atif Aslam"
#     d1['img']=res['album']['images'][0]['url']
#     d1['src']=res['preview_url']
#     info_songs.append(d1)
# # print(info_songs)
# print(sp.featured_playlists(locale=None, country="IN", timestamp=None, limit=20, offset=0))
# print(sp.artist('spotify:artist:4YRxDV8wJFPHPTeXepOstw')['images'][0]['url'])
# print(info_songs)
# return info_songs
# for res in result:
#     pprint.pprint(res)

search_str = 'pal ek pal'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search(search_str,limit=48)
info_songs= list()
for res in result['tracks']['items']:
    # print(res['name'])  #track name
    # print(res['album']['images'][0]['url'])  #track image
    # print(res['preview_url'])    #track url 
    info_songs.append([res['name'],res['album']['images'][0]['url'],res['preview_url']])
song =info_songs[0]
allMusic=list()
d1 =dict()
d1['name']=song[0]
d1['artist'] =' '
d1['img']=song[1]
d1['src']=song[2]
allMusic.append(d1)
    # print("name: ",song[0])
    # print("artist: ",' ')
    # print("img_info: ",song[1])
    # print("srcSong: ",song[2])

print(allMusic[0]['name'])
print(allMusic[0]['artist'])
print(allMusic[0]['img'])
print(allMusic[0]['src'])
print(allMusic)
# allMusic=list()
# songNum=0
# d1 =dict()
# d1['name']=name
# d1['artist'] =artist
# d1['img']=img_info
# d1['src']=srcSong
# allMusic.append(d1)