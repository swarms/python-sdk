import json
import re
import requests


class Client:
    def __init__(self, base_url, username, password):
        self.base_url = re.sub("/$", "", base_url)
        self.username = username
        self.password = password
        self.auth_token = None

    def set_auth_token(self, auth_token):
        self.auth_token = auth_token

    default_headers = {
        "Content-Type": "application/json",
        "Accept": "application/hal+json",
    }

    def headers(self):
        if self.auth_token:
            return self.default_headers + {"X-Auth-Token": self.auth_token}
        return self.default_headers

    def get(self, url):
        return requests.get(self.base_url + url, headers=self.headers())

    def post(self, url, payload):
        return requests.post(self.base_url + url, headers=self.headers(), data=json.dumps(payload))

    def put(self, url, payload):
        return requests.put(self.base_url + url, headers=self.headers(), data=json.dumps(payload))
