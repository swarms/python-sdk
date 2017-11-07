import json
import client_builder
from client import campaigns, jobs


client = client_builder.build()

campaign = campaigns.create(client, {
    "name": "My zen campaign",
    "title": "Zen campaign",
    "estDuration": "30 seconds",
    "workerPayment": 0.1,
    "results": 100,
})

job1 = jobs.create(client, {
    "name": "Solve koans"
})

job2 = jobs.create(client, {
    "name": "Meditate"
})

campaigns.add_jobs(client, campaign, [job1, job2])

# TODO add tasks


# You need to top up your account to publish the campaign!
# campaigns.publish(client, campaign)

campaign_list = campaigns.get_all(client)
print(json.dumps(campaign_list))

job_list = jobs.get_all(client)
print(json.dumps(job_list))
