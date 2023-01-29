from plexapi.server import PlexServer
from plexapi.myplex import MyPlexAccount
from pymongo import MongoClient
from pprint import *

from config import *

if config[PLEX][APITOKEN]:
    print('using token')
    # plex = PlexServer('http://localhost:32400', 'your_token')
    plex = PlexServer(f'http://{config[PLEX][SERVERNAME]}:32400', config[PLEX][APITOKEN])
else:
    print('using user and pass')
    plexAccount = MyPlexAccount(config[PLEX][USER], config[PLEX][PASS])
    plex = plexAccount.resource(config[PLEX][SERVERNAME]).connect() 

print(plex._token)

client = MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["watchlist"]
collectionMovies = db["movies"]
print(f'Finding movie: {collectionMovies.find().sort("title")[0]["title"]}')

movie = plex.library.search(guid=collectionMovies.find().sort("title")[0]['guid'])[0] 
pprint(f'title = {movie.title} duration = {movie.duration} '
    )


# getGuid(self, guid)
# movie = plex.library.search(title='The Shawshank Redemption')[0]
# movie_guid = movie.guid

# client = plex.client(config[PLEX][CLIENTNAME])

# client.playMedia(guid=movie_guid)
