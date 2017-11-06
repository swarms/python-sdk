import json
import client_builder
from client import campaigns

client = client_builder.build()

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
