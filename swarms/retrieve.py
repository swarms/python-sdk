import json
import config
from sdk import services


campaigns, jobs, tasks, results = services.get(config)

print("")
print("Campaigns:")
campaign_list = campaigns.get_all()
for campaign in campaign_list["campaigns"]:
    print("  %s  %s  %s" % (campaign["id"], campaign["name"], campaign["title"]))

    print("")
    print("  Results:")
    result_list = campaigns.results(campaign)
    for result in result_list["jobResults"]:
        print("    %s" % json.dumps(result))


print("")
print("Jobs:")
job_list = jobs.get_all()
for job in job_list["jobs"]:
    print("  %s  %s" % (job["id"], job["name"]))

print("")
print("Tasks:")
task_list = tasks.get_all()
for task in task_list["tasks"]:
    print("  %s  %s" % (task["id"], task["name"]))
