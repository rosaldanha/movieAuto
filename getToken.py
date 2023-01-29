import requests
from config import *
url = 'https://plex.tv/users/sign_in.json'
payload = {'user[login]': config[PLEX][USER], 'user[password]': config[PLEX][PASS]}

print (payload)
r = requests.post(url, data=payload)

if r.status_code == 201:
    print(r.json()['user']['authentication_token'])
else:
    print('Error: Could not find token')

# just a test