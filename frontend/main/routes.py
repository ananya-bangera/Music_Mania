from asyncio.windows_events import NULL
from flask import render_template, request, Blueprint
from frontend.models import Post
import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials
from flask import render_template, url_for, flash, session,redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from frontend.models import User, Post
from flask import Flask, request, render_template 
import forms
import sys
uri_dict=dict()
data_dict=dict()
main = Blueprint('main', __name__)
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

@main.route('/')
# @main.route("/searchbar")
@main.route("/home")
def home():
    # Main_list=list()
    # for artist_uri in uri_dict.values:
    #     list.append(data(artist_uri))
    return render_template('home.html',uri_dict=uri_dict, spotify=spotify)
# def data(artist_uri):
#     pass

@main.route("/searchbar", methods =["GET", "POST"])
def searchbar():
    if request.method == "POST":
       data = request.form.get("search-bar-ani")
       if data == NULL or data==" " or data == "":
           return redirect(url_for('main.home'))
       info_req = info(data)
       return render_template("songs.html",info_req=info_req,data=data,i=0)
    return render_template("home.html")

def info(data):
    search_str = data
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    result = sp.search(search_str,limit=48)
    info_songs= list()
    iter_song=0
    n = random.randint(1,1000)
    data_dict[n]=data
    for res in result['tracks']['items']:
        # print(res['name'])  #track name
        # print(res['album']['images'][0]['url'])  #track image
        # print(res['preview_url'])    #track url 
        if res['preview_url'] is not None:
            if res['name'] is not None:
                if res['album']['images'][0]['url'] is not None:
                    info_songs.append([res['name'],res['album']['images'][0]['url'],res['preview_url'],iter_song,n])
                    iter_song=iter_song+1
    return info_songs

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/media_player")
def media_player():
    return render_template('media_player.html', title='About')

@main.route("/contact")
def contact():
    return render_template('contact.html', title='Contact Us')

@main.route("/thanks")
def thanks():
    return render_template('thanks.html', title='Thank You')

@main.route("/feedback")
def feedback():
    return render_template('feedback.html', title='Feedback')

@main.route("/tracking")
def tracking():
    return render_template('tracking.html', title='Tracker')

@main.route("/tracks/<name>/<album_name>", methods=['GET', 'POST'])
def tracks(name,album_name):
    Album_details=Artist(name)
    val=fetchAlbum(album_name,Album_details)
    return render_template('tracks.html', title='Tracks',name=name, Album_details=Album_details,val=val,album_name=album_name)

@main.route("/albums/<name>", methods=['GET', 'POST'])
def albums(name):
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    Album_details=Artist(name)
    return render_template('albums.html', title='Albums',name=name,Album_details=Album_details)

@main.route("/songsList/<name>/<album_name>/<songInfo>", methods=['GET', 'POST'])
def songsList(name,album_name,songInfo):
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    # Album_details=Artist(name)
    Album_details=Artist(name)
    val=fetchAlbum(album_name,Album_details)
    allMusic= musiclist(name,Album_details,val)
    songNum=fetchTrack(songInfo,allMusic)
    return render_template('media_player.html', title='Media Player',songNum=songNum,album_name=album_name,name=name,val=val,allMusic=allMusic)

@main.route("/wish/<name>/<songName>/<path:img_info>/<path:srcSong>/<int:data>/<int:eachsongNum>", methods=['GET', 'POST'])
def wish(name,songName,img_info,srcSong,data,eachsongNum):
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    # songName.replace("%20"," ")
    
    info_req = info(data_dict[data])
    # numVal2 =fetchWork2(info_req,songName)
    # numVal =int(fetchWork(info_req,songName))
    numVal =eachsongNum
    allMusic=list()
    d1 =dict()
    d1['name']=info_req[eachsongNum][0]
    d1['artist'] =' '
    d1['img']=info_req[eachsongNum][1]
    d1['src']=info_req[eachsongNum][2]
    allMusic.append(d1)
    # print(allMusic)
    # print('This is error output', file=sys.stderr)
    return render_template('media_player.html', title='Media Player',songNum=0,allMusic=allMusic)

# =========> uri routes
def Artist(name):
    return Uri(uri_dict[name])




# ==========> song fetching routes
def Uri(uri):
    l=spotify.artist_albums(uri,limit=18)
    Album_details=dict()
    i=0
    for AlbumItem in l['items']:
        i=i+1
        album_id = AlbumItem['uri']
        Album_name=[AlbumItem['name'],AlbumItem['images']]
        res = spotify.album_tracks(album_id)
        track_details=list()
        for track in res['items']:
            track_details.append([track['name'],track['preview_url']])
        Album_details[i]=[Album_name,track_details]
    return Album_details

def fetchAlbum(album_name,Album_details):
    val =1
    for name in Album_details.values():
        if(name[0][0]==album_name):
            return val
        val=val+1

def fetchWork(info_req,songName):
    val =0
    for song in info_req:
        if(song[0]==songName):
            if(val>=len(info_req)):
                return 0
            return val
        val=val+1
    return 0

def fetchWork2(info_req,songName):
    val =0
    for song in info_req:
        if(song[0]==songName):
            # if(val>=len(info_req)):
            #     return 0
            return val
        val=val+1
    

def fetchTrack(songInfo,allMusic):
    trackval=0
    for songName in allMusic:
        if(songName['name']==songInfo):
            return trackval
        trackval=trackval+1

def musiclist(name,Album_details,val):
    allMusic = list()
    for item in Album_details[val][1]:
        d1 =dict()
        d1['name']=item[0]
        d1['artist'] =name
        d1['img']=Album_details[val][0][1][0]['url']
        d1['src']=item[1]
        allMusic.append(d1)
    return allMusic 



uri_dict = {"Arijit Singh":'spotify:artist:4YRxDV8wJFPHPTeXepOstw',"Atif Aslam":'spotify:artist:2oSONSC9zQ4UonDKnLqksx',
"Armaan Malik":'spotify:artist:4IKVDbCSBTxBeAsMKjAuTs',"Neha Kakkar":'spotify:artist:5f4QpKfy7ptCHwTqspnSJI',
"Dhvani Bhanushali":'spotify:artist:1OPqAyxsQc8mcRmoNBAnVk',"Justin Bieber":'spotify:artist:1uNFoZAHBGtllmzznpCI3s',
"Jasleen Royal":'spotify:artist:74OaRjmyh0XyRZsQQQ5l7c',"Tony Kakkar":'spotify:artist:0NZtn1Kyq08alpHCTRf3dv',
"Emiway Bantai":'spotify:artist:008PpLcKUtVXle6JSwkq3I',"Raftar":'spotify:artist:5UdFr0GeO7jKIaNIJgwB36',
"Javed Ali":'spotify:artist:4W91bbPB2CTSsHwt7eqNl7',"Jubin Nautiyal":'spotify:artist:1tqysapcCh1lWEAc9dIFpa'}
