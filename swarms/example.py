from client import Client
from client.auth import authenticate


client = Client("http://localhost:9040/", "ash.ketchum@alabastia.pkm", "pickachu")
authenticate(client)
