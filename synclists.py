from pprint import pprint
from watchlist import WatchList
from video import Video,Show
from pymongo import MongoClient
from config import *

def isOnWatchList(videoGuid, watchList):
    for video in watchList:
        if video.guid == videoGuid:
            return True
    return False


client = MongoClient(config[MONGO_URL])
db = client["watchlist"]
moviesCollection = db["movies"]
showsCollection = db["shows"]

watchList = WatchList()
watchListMovies = watchList.getWatchListMovies()
# add new movies
for movie in watchListMovies:
    tmpVideo = Video(title=movie.title, guid=movie.guid)
    if moviesCollection.count_documents({"guid": movie.guid}) == 0:        
        print(tmpVideo.title)
        moviesCollection.insert_one(vars(tmpVideo))
    else:
        print(f'{tmpVideo.title} já cadastrado no db')
# remove watched
for movie in moviesCollection.find():
    if not isOnWatchList(movie['guid'],watchListMovies):
        moviesCollection.delete_one({"guid":movie['guid']}) 

watchListShows = watchList.getWatchListShows()
for show in watchListShows:
    tmpShow = Show(title=show.title,guid=show.guid,episodes=None)
    if showsCollection.count_documents({"guid": show.guid}) == 0:
        print(f'Show: {tmpShow.title} added')
        showsCollection.insert_one(vars(tmpShow))
    else:
        print(f'Show {tmpShow.title} already exists on db')

for show in showsCollection.find():
    if not isOnWatchList(show['guid'],watchListShows):
        showsCollection.delete_one({"guid":show['guid']}) 
