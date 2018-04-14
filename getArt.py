import spotipy
import spotipy.util as util

def getCredentials(filename):
	fin = open(filename).read()
	return(fin.split("\n")[:-1])

username, client_id, client_secret = getCredentials("secret")
redirect_uri = 'https://example.com/callback/'
scope = 'user-read-currently-playing'

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

sp = spotipy.Spotify(token)

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

results = sp.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print ('track    : ' + track['name'])
    print ('audio    : ' + track['preview_url'])
    print ('cover art: ' + track['album']['images'][0]['url'])
    print ()
