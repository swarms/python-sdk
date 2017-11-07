import sys
import client_builder
from client import Client, exceptions, auth, campaigns, jobs

sys.exit("You'll have to comment out this line to be able to delete all your stuff...")

client = client_builder.build()

job_list = jobs.get_all(client)
for job in job_list["jobs"]:
    print("deleting job %i: %s" % (job["id"], job["name"]))
    jobs.delete(client, job)

campaign_list = campaigns.get_all(client)
for campaign in campaign_list["campaigns"]:
    print("deleting campaign %i: %s" % (campaign["id"], campaign["name"]))
    try:
        # currently running campaigns can't be deleted
        campaigns.cancel(client, campaign)
    except exceptions.HalLinkNotFound:
        pass

    campaigns.delete(client, campaign)
