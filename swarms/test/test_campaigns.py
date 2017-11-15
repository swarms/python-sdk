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

    def test_campaigns_publish(self):
        self.campaigns.publish({
            "_links": {
                "publish": {
                    "href": "/campaigns/3/publish"
                }
            }
        })

    def test_campaigns_cancel(self):
        self.campaigns.cancel({
            "_links": {
                "cancel": {
                    "href": "/campaigns/3/cancel"
                }
            }
        })

    def test_campaigns_pause(self):
        self.campaigns.pause({
            "_links": {
                "pause": {
                    "href": "/campaigns/3/pause"
                }
            }
        })

    def test_campaigns_continue(self):
        self.campaigns.cont({
            "_links": {
                "continue": {
                    "href": "/campaigns/3/continue"
                }
            }
        })

    def test_get_campaign_jobs(self):
        jobs = self.campaigns.get_jobs({
            "_links": {
                "jobs": {
                    "href": "/campaigns/3/jobs"
                }
            }
        })
        self.assertEqual(jobs["jobs"][0]["name"], "My first Job")

    def test_add_campaign_jobs(self):
        self.campaigns.add_jobs({
            "_links": {
                "jobs": {
                    "href": "/campaigns/3/jobs"
                }
            }
        }, [{"id": 1}, {"id": 2}, {"id": 3}])

    def test_update_campaign_jobs(self):
        self.campaigns.update_jobs({
            "_links": {
                "jobs": {
                    "href": "/campaigns/3/jobs"
                }
            }
        }, [{"id": 1}, {"id": 2}, {"id": 3}])

    def test_get_results(self):
        results = self.campaigns.results({
            "_links": {
                "results": {
                    "href": "/campaigns/3/results"
                }
            }
        })

if __name__ == '__main__':
    unittest.main()
