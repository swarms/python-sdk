import sys
import config
from sdk import services, exceptions


# sys.exit("You'll have to comment out this line to be able to delete all your stuff...")

campaigns, jobs, tasks, results = services.get(config)

task_page = tasks.next_page()
for task in task_page["tasks"]:
    print("deleting task %i: %s" % (task["id"], task["name"]))
    tasks.delete(task)

job_page = jobs.next_page()
for job in job_page["jobs"]:
    print("deleting job %i: %s" % (job["id"], job["name"]))
    jobs.delete(job)

campaign_page = campaigns.next_page()
for campaign in campaign_page["campaigns"]:
    print("deleting campaign %i: %s" % (campaign["id"], campaign["name"]))
    try:
        # currently running campaigns can't be deleted
        campaigns.cancel(campaign)
    except exceptions.HalLinkNotFound:
        pass

    campaigns.delete(campaign)
