import json


def authenticate(client):
    response = client.post("/auth/token/request", {
        "email": client.username,
        "password": client.password,
    })

    auth_token = json.loads(response.content.decode())["accessToken"]
    client.set_auth_token(auth_token)

    return response
