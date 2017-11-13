import json
import config
from sdk import services


campaigns, jobs, tasks, results = services.get(config)

print("")
print("Campaigns:")
campaign_list = None
while True:
    campaign_list = campaigns.next_page(campaign_list)

    if campaign_list is None:
        break

    for campaign in campaign_list["campaigns"]:
        print("  %s  %s  %s" % (campaign["id"], campaign["name"], campaign["title"]))

        print("")
        print("  Results:")
        result_list = campaigns.results(campaign)
        print(result_list)
        while result_list is not None:
            for result in result_list["jobResults"]:
                print("    %s" % json.dumps(result))

            result_list = campaigns.next_page(result_list)


print("")
print("Jobs:")
job_list = None
while True:
    job_list = jobs.next_page(job_list)

    if job_list is None:
        break

    for job in job_list["jobs"]:
        print("  %s  %s" % (job["id"], job["name"]))


print("")
print("Tasks:")
task_list = None
while True:
    task_list = tasks.next_page(task_list)

    if task_list is None:
        break

    for task in task_list["tasks"]:
        print("  %s  %s" % (task["id"], task["name"]))
