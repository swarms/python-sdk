import json
import config
from sdk import services


campaigns, jobs, tasks, results = services.get(config)

print("")
print("Campaigns:")
for campaign in campaigns.get_all():
    print("  %s  %s  %s" % (campaign["id"], campaign["name"], campaign["title"]))

    print("")
    print("  Results:")
    result_list = campaigns.get_all_results(campaign)
    for result in result_list:
        print("    %s" % json.dumps(result))


print("")
print("Jobs:")
for job in jobs.get_all():
    print("  %s  %s" % (job["id"], job["name"]))


print("")
print("Tasks:")
for task in tasks.get_all():
    print("  %s  %s" % (task["id"], task["name"]))
