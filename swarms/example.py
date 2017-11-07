import json
import config
from client import services

campaigns, jobs = services.get(config)


campaign = campaigns.create({
    "name": "My zen campaign",
    "title": "Zen campaign",
    "estDuration": "30 seconds",
    "workerPayment": 0.1,
    "results": 100,
})

job1 = jobs.create({
    "name": "Solve koans"
})

job2 = jobs.create({
    "name": "Meditate"
})

campaigns.add_jobs(campaign, [job1, job2])

# TODO add tasks


# You need to top up your account to publish the campaign!
# campaigns.publish(client, campaign)

campaign_list = campaigns.get_all()
print(json.dumps(campaign_list))

job_list = jobs.get_all()
print(json.dumps(job_list))
