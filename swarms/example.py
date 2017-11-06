import json
from client import Client, auth, campaigns


client = Client("http://localhost:9040/", "ash.ketchum@alabastia.pkm", "pickachu")
auth.authenticate(client)

campaign = campaigns.create(client, {
    "name": "My zen campaign",
    "title": "Record the sound of one hand clapping",
    "estDuration": "30 seconds",
    "workerPayment": 0.1,
    "results": 100,
})

# TODO jobs and tasks

campaigns.publish(client, campaign)

campaign_list = campaigns.get_all(client)
print(json.dumps(campaign_list))
