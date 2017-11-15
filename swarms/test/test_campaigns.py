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

    def test_campaigns_get_page(self):
        page = self.campaigns.get_page()
        self.assertEqual(page["campaigns"][0]["name"], "My first Campaign")

    def test_campaigns_get_one(self):
        campaign = self.campaigns.get(3)
        self.assertEqual(campaign["name"], "My first Campaign")

    def test_campaigns_update(self):
        campaign = self.campaigns.update({
            "name": "My zen campaign",
            "title": "Zen campaign",
            "_links": {
                "self": {
                    "href": "/campaigns/3"
                }
            }
        })
        self.assertEqual(campaign["name"], "My first Campaign")

    def test_campaigns_delete(self):
        self.campaigns.delete({
            "_links": {
                "self": {
                    "href": "/campaigns/3"
                }
            }
        })

if __name__ == '__main__':
    unittest.main()
