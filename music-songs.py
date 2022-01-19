from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import eel
# eel.init('frontend')
# search_str = 'Atif Aslam'
# @eel.expose
# def musiclist():
uri = 'spotify:artist:4YRxDV8wJFPHPTeXepOstw'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
l=sp.artist_albums(uri,limit=18)
Album_details=dict()
i=0
for AlbumItem in l['items']:
    i=i+1
    album_id = AlbumItem['uri']
    Album_name=[AlbumItem['name'],AlbumItem['images']]
    res = sp.album_tracks(album_id)
    track_details=list()
    for track in res['items']:
        track_details.append([track['name'],track['preview_url']])
    Album_details[i]=[Album_name,track_details]
val = 1
print(Album_details[val][0][1][0]['url'])
# trackval=0
# album_name='Swag Se Swagat (From "Tiger Zinda Hai")'
# val =1
# trackval=0
# songInfo ='Khuda Jaane Revisited - Remix'
# # for name in Album_details[1][1]:
# #     if(name[0]==songInfo):
# #         print(trackval)
# #     trackval=trackval+1
# val =2
# name = "Atif"
# # ==>
# # d1 =dict()
# allMusic = list()
# print(Album_details[val][1])
# for item in Album_details[val][1]:
#     d1 =dict()
#     d1['name']=item[0]
#     d1['artist'] =name
#     d1['img']=Album_details[val][0][1][0]['url']
#     d1['src']=item[1]
#     # print(d1)
#     allMusic.append(d1)   
# # print(allMusic)

# trackval=0
# for song in allMusic:
#     if(song['name']==songInfo):
#         print(trackval)
#     trackval=trackval+1
# # for i in range(len(allMusic)):
# #         # if(name[0]==album_name):
#     print(allMusic[i])
            # break
        # trackval=trackval+1
# print(allMusic[trackval])

#     result = sp.search(search_str,limit =50)
#     # print(result)
#     allMusic= list()
#     d1 =dict()
#     for res in result['tracks']['items']:
#         d1['name']=res['name']
#         d1['artist'] ="Atif Aslam"
#         d1['img']=res['album']['images'][0]['url']
#         d1['src']=res['preview_url']
#         allMusic.append(d1)
#     return allMusic
# eel.start('home.html')
