import sys
from client import Client, auth, campaigns, exceptions

sys.exit("You'll have to comment out this line to be able to delete all your stuff...")

client = client_builder.build()

campaign_list = campaigns.get_all(client)
for campaign in campaign_list["campaigns"]:
    try:
        # currently running campaigns can't be deleted
        campaigns.cancel(client, campaign)
    except exceptions.HalLinkNotFound:
        pass

    campaigns.delete(client, campaign)
