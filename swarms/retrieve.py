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
    result_list = campaigns.results(campaign)
    while result_list is not None:
        for result in result_list["jobResults"]:
            print("    %s" % json.dumps(result))

        result_list = campaigns.next_page(result_list)


print("")
print("Jobs:")
for job in jobs.get_all():
    print("  %s  %s" % (job["id"], job["name"]))


print("")
print("Tasks:")
for task in tasks.get_all():
    print("  %s  %s" % (task["id"], task["name"]))
