import json
from exceptions import UnexpectedHTTPStatusCode


def authenticate(client):
    response = client.post("/auth/token/request", {
        "email": client.username,
        "password": client.password,
    })

    if response.status_code == 200:
        client.auth_token = json.loads(response.content)["accessToken"]
    else:
        raise UnexpectedHTTPStatusCode()

    return response
