import json
import re
import requests

from .exceptions import UnexpectedHTTPStatusCode


class Client:
    def __init__(self, base_url, username, password):
        self.base_url = re.sub("/$", "", base_url)
        self.username = username
        self.password = password

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/hal+json",
    }

    def set_auth_token(self, auth_token):
        self.headers["X-Auth-Token"] = auth_token

    def handle_response(self, response):
        if response.status_code >= 200 and response.status_code < 300:
            content = response.content.decode()
            if len(content) > 0:
                return json.loads(content)
            else:
                return {}
        else:
            raise UnexpectedHTTPStatusCode(response.status_code, response.content)

    def get(self, url):
        request = requests.get(self.base_url + url, headers=self.headers)
        return self.handle_response(request)

    def post(self, url, payload = None):
        request = requests.post(self.base_url + url, headers=self.headers, data=json.dumps(payload))
        return self.handle_response(request)

    def put(self, url, payload):
        request = requests.put(self.base_url + url, headers=self.headers, data=json.dumps(payload))
        return self.handle_response(request)

    def delete(self, url):
        request = requests.delete(self.base_url + url, headers=self.headers)
        return self.handle_response(request)
