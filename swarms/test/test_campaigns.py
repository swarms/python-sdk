import unittest
from ..sdk import Client, Campaigns
from . import config


class CampaignsTest(unittest.TestCase):
    client = Client(config.base_url, config.username, config.password)
    campaigns = Campaigns(client)

    def test_campaigns_create(self):
        self.campaigns.create({
            "name": "My zen campaign",
            "title": "Zen campaign",
            "estDuration": "30 seconds",
            "workerPayment": 0.1,
            "results": 100,
        })

    def test_campaigns_get(self):
        page = self.campaigns.get_page()
        self.assertEqual(page["campaigns"][0]["name"], "My first Campaign")

    def test_campaigns_update(self):
        pass
        #updated = self.campaigns.update({
        #    "name": "My zen campaign",
        #    "title": "Zen campaign",
        #    "estDuration": "30 seconds",
        #    "workerPayment": 0.1,
        #    "results": 100,
        #    "_links": {
        #        "self": {
        #            "href": config.base_url + "campaigns/3"
        #        }
        #    }
        #})
        #self.assertEqual(updated["name"], "My first Campaign")

if __name__ == '__main__':
    unittest.main()