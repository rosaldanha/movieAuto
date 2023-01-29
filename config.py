import yaml
from dotenv import load_dotenv
from os import environ


# CONSTANTS #################################
MOVIESECTION            = 'movieSection'
STREAMINGSERVICELIST    = 'streamingServicesList'
MYSTREAMINGSERVICES     = 'myStreamingServices'
PLEX                    = 'plex'
SERVERNAME              = 'serverName'
USER                    = 'user'
PASS                    = 'pass'
CLIENTNAME              = 'clientName'
APITOKEN                = 'apiToken'
MONGO_URL               = 'mongoUrl'



config = ''
with open('config.yml') as f:
    config = yaml.safe_load(f)
# load secrets
load_dotenv(dotenv_path='./secrets.env')
# adjust sensitive variables
config[PLEX][PASS]      = environ.get('PLEXPASSWORD')
config[PLEX][APITOKEN]  = environ.get('PLEXAPITOKEN')
config[MONGO_URL]       = environ.get('MONGOURL')

print(config)