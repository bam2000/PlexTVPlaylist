from plexapi.server import PlexServer
import random

baseurl = input("Type ip and port of your Plex server:")
token = input("Type your authentication token (https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/):")
plex = PlexServer("http://" + baseurl, token)


TVShows = []
Episodes = []
PlayList = []
fileoftvshows = open("Shows.txt", "r")

movies = plex.library.section('Movies')
for video in movies.search(unwatched=True):
    print(video.title)
