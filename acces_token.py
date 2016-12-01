"""
Script to get your access token.
Access token is needed for API calls.
"""
import requests

# Step Zero: Get necessary information
client_id = input("Client ID: ").strip()
client_secret = input("Client Secret: ").strip()
redirect_uri = input("Redirect URI: ").strip()
raw_scope = input("Requested scope (separated by spaces, blank for just basic read): ").strip()
scope = raw_scope.split(' ')
if not scope or scope == [""]:
    scope = ["basic"]

# Step One: Direct your user to our authorization URL
print("Visit this page and authorize access in your browser:\n")
print("https://api.instagram.com/oauth/authorize?client_id="+client_id+"&redirect_uri="+redirect_uri+"&response_type=code")
print("\n")

# Step Two: Receive the redirect from Instagram
code = (str(input("Paste in code found after 'q=' in the url: ").strip()))

# Step Three: Request the access_token
client_params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "grant_type": "authorization_code",
    "code": code
}
r = requests.post('https://api.instagram.com/oauth/access_token', data=client_params)
data = r.json()
print("Successfully received access_token")
print("Username: " + data['user']['username'])
print("User id: " + data['user']['id'])
print("Access token: " + data['access_token'])
