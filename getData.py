import spotipy
import spotipy.util as util
from tqdm import tqdm

def getCredentials(filename):
	fin = open(filename).read()
	return(fin.split("\n")[:-1])

def getSp():

    username, client_id, client_secret = getCredentials("secret")
    redirect_uri = 'https://example.com/callback/'
    scope = 'user-read-currently-playing'

    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    sp = spotipy.Spotify(token)
    return sp

def getInfo(id, sp):
    track = sp.track(id)
    artist = sp.artist(track['artists'][0]['id'])

    name = track['name'].replace(',', '')
    album = track['album']['name'].replace(',', '')
    arts = []
    imgs = track['album']['images']
    for img in imgs:
        arts.append(img['url'])

    arts = "+".join(arts)

    genres = artist['genres']
    genres = "+".join(genres)
    return ", ".join([name, album, arts, genres])

def getData(file):
    file = open(file, 'r').read().split('\n')
    f = open('out', 'w')

    sp = getSp()
    
    for id in tqdm(file):
        f.write(getInfo(id, sp) + '\n')


getData('ids')
