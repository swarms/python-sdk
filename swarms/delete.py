import sys
import config
from sdk import services, exceptions


sys.exit("You'll have to comment out this line to be able to delete all your stuff...")

campaigns, jobs, tasks, results = services.get(config)

task_list = tasks.get_all()
for task in task_list["tasks"]:
    print("deleting task %i: %s" % (task["id"], task["name"]))
    tasks.delete(task)

job_list = jobs.get_all()
for job in job_list["jobs"]:
    print("deleting job %i: %s" % (job["id"], job["name"]))
    jobs.delete(job)

campaign_list = campaigns.get_all()
for campaign in campaign_list["campaigns"]:
    print("deleting campaign %i: %s" % (campaign["id"], campaign["name"]))
    try:
        # currently running campaigns can't be deleted
        campaigns.cancel(campaign)
    except exceptions.HalLinkNotFound:
        pass

    campaigns.delete(campaign)
