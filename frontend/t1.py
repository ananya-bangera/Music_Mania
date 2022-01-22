# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
arijit_uri = 'spotify:artist:4YRxDV8wJFPHPTeXepOstw'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# results = spotify.artist_albums(arijit_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])


#=========>Tracks name song and pic
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(arijit_uri)
# results = spotify.album_tracks(arijit_uri,limit=50, offset=0, market=None)
# print(results)
for track in results['tracks'][:3]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    


print(">>"*100)
l=spotify.artist_albums(arijit_uri)
print(l)
print("*"*100)
# print(res)
# print("*"*100)
# ==============>to listdown uri of given artsis id 
# for AlbumItem in l['items']:
#     album_id = AlbumItem['uri']
#     print("Album name: "+AlbumItem['name'])
#     res = spotify.album_tracks(album_id)
#     # print(res['items'])
#     for track in res['items']:
#         print('track    : ' + track['name'])
#         print('audio:',end=" ")
#         print( track['preview_url'])
#         print("-"*100)
#     print("*"*100)

l=spotify.artist_albums(arijit_uri)
Album_details=dict()
i=0
for AlbumItem in l['items']:
    i=i+1
    album_id = AlbumItem['uri']
    Album_name=[AlbumItem['name'],AlbumItem['images']]
    res = spotify.album_tracks(album_id)
    track_details=list()
    for track in res['items']:
        # print(track)
        track_details.append([track['name'],track['preview_url']])
        # print(spotify.audio_analysis('spotify:track:7vTgjzH5IPaMsi8cvNd8cD'))
        # print("-"*100)
    # print(track_details)
    # print()

    Album_details[i]=[Album_name,track_details]
# for i in Album_details.keys():
    # print(Album_details[i][1])
    # print()
    # print()
# for song in Album_details[1][1]:
    # print(song[0])                        
    # print(song[1])                        
    # print(type(song))                        
# for name in Album_details.values():
#     print(name[0][0])  #names of album
#     print(name[0][1][0]['url'])  #pics of album
#     print("*"*100)
# for name in Album_details.values():
    # print(name[1])  #songs
#     print(name[0][0])  #names of album
#     print(name[0][1][0]['url'])  #pics of album
print("*"*100)

# val =1
# for name in Album_details.values():
#     if(name[0][0]==provided):
#         return val
    # val=val+1
#     print(name[0][0])  #names of album
#     print(name[0][1][0]['url'])  #pics of album
    # print("*"*100)
# print(Album_details)

print(spotify.artist('Arijit Singh')) 
# print("-"*100)
# print(spotify.track('spotify:track:0WdbnNKO0Jt4BZACSDQh44')) 
# print(spotify.artist_top_tracks(arijit_uri))
# q='name: Arijit Singh'
# print(spotify.search(q, limit=20, offset=0, type= 'track,artist',include_external='audio'))
# print(spotify.search(q, limit=10, offset=0, type= 'track,artist')['artists'])





    # tracks name>>> Album_details[1][1][i][0]
    # tracks audio url>>> Album_details[1][1][i][1]
# print(Album_details[1][1][0][1])
# print(p[1][1][0][0])
# print(Album_details[1][1][0][0])


# print(l['items'][0]['uri'])
# print("*&&"*100)
# print(l['items'])
# print("*%*"*100)
# print(l['items'][0])
# print("-"*100)
# print(l['items'][1])
# print("-"*100)
# print(l['items'][2])
# print("-"*100)
# print(l['items'][3])
# print("*"*100)
# print(l['items'][0]['artists'])
# print("*"*100)
# print(l['items'][0]['artists'][0])
# print(l['items'][0]['artists'][1])
# print(l['items'][0]['artists'][2])
# print(l['items'][0]['artists'][3])
print("*"*100)
# to get uri of artists
# print(l['items'][0]['artists'][0]['uri'])
# print(l['items'][0]['artists'][1]['external_urls']['spotify'])
# print(l['items'][0]['artists'][2]['id'])
# print("*%*"*100)
# print(l['items'][0]['album'])
# external url >>> spotify
# for track in l['albums'][:5]:
#     print('album:    : ' + track)
    # print('audio    : ' + track['preview_url'])
    # print('cover art: ' + track['album']['images'][0]['url'])
    # print()
# print(l)

#=========>Artist pic
# import spotipy
# import sys
# from spotipy.oauth2 import SpotifyClientCredentials

# spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# if len(sys.argv) > 1:
#     name = ' '.join(sys.argv[1:])
# else:
#     name = 'Arijit'

# results = spotify.search(q='artist:' + name, type='artist')
# items = results['artists']['items']
# if len(items) > 0:
#     artist = items[0]
#     print(artist['name'], artist['images'][0]['url'])
