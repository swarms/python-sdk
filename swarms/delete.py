import config
from sdk import services, exceptions


# sys.exit("You'll have to comment out this line to be able to delete all your stuff...")

campaigns, jobs, tasks, results = services.get(config)

for task in tasks.get_all():
    print("deleting task %i: %s" % (task["id"], task["name"]))
    tasks.delete(task)

for job in jobs.get_all():
    print("deleting job %i: %s" % (job["id"], job["name"]))
    jobs.delete(job)

for campaign in campaigns.get_all():
    print("deleting campaign %i: %s" % (campaign["id"], campaign["name"]))
    try:
        # currently running campaigns can't be deleted
        campaigns.cancel(campaign)
    except exceptions.HalLinkNotFound:
        pass

    campaigns.delete(campaign)
