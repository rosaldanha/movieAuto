from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from config import *

class WatchList():

    def __init__(self) -> None:    
        self.plexAccount = MyPlexAccount(config[PLEX][USER], config[PLEX][PASS])
        self.plex = self.plexAccount.resource(config[PLEX][SERVERNAME]).connect()  # returns a PlexServer instance
        
 
    def getWatchListMovies(self):
        return self.plexAccount.watchlist(filter='available',libtype='movie',sort='titleSort:asc')

    def getWatchListShows(self):
        return self.plexAccount.watchlist(filter='available',libtype='show',sort='titleSort:asc')