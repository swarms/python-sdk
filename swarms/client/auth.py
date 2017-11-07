class Auth:
    def __init__(self, client):
        self.client = client

    def authenticate(self):
        response = self.client.post("/auth/token/request", {
            "email": self.client.username,
            "password": self.client.password,
        })

        auth_token = response["accessToken"]
        self.client.set_auth_token(auth_token)

        return response
