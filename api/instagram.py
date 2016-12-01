import requests


class Instagram:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_users_self(self):
        params = {
            "access_token": self.access_token
        }
        r = requests.get('https://api.instagram.com/v1/users/self/', params=params)
        return r.json()


