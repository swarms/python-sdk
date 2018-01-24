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

    def token_headers(self):
        return {"X-Auth-Token": self.headers["X-Auth-Token"]}

    @staticmethod
    def handle_response(response):
        if 200 <= response.status_code < 300:
            content = response.content.decode('utf-8')
            if len(content) > 0:
                return json.loads(content)
            else:
                return {}
        else:
            raise UnexpectedHTTPStatusCode(response.status_code, response.content)

    def get(self, url):
        response = requests.get(self.base_url + url, headers=self.headers)
        return self.handle_response(response)

    def post(self, url, payload=None):
        response = requests.post(self.base_url + url, headers=self.headers, data=json.dumps(payload))
        return self.handle_response(response)

    def post_file(self, url, name, content, mimetype):
        response = requests.post(
            self.base_url + url,
            headers=self.token_headers(),
            files={'file': (name, content, mimetype)}
        )

        return self.handle_response(response)

    def put(self, url, payload):
        response = requests.put(self.base_url + url, headers=self.headers, data=json.dumps(payload))
        return self.handle_response(response)

    def delete(self, url):
        response = requests.delete(self.base_url + url, headers=self.headers)
        return self.handle_response(response)
