import requests


class Instagram:
    def __init__(self, access_token):
        self.params = {
            "access_token": access_token
        }

    def get_users_self(self):
        r = requests.get('https://api.instagram.com/v1/users/self/', params=self.params)
        return r.json()

    def get_users(self, user_id):
        r = requests.get('https://api.instagram.com/v1/users/' + user_id + '/', params=self.params)
        return r.json()


