from .utils.hal import get_link
from . import BaseService


class Campaigns(BaseService):
    def __init__(self, client):
        self.client = client

    # crud
    def create(self, campaign):
        return self.client.post("/campaigns", campaign)

    def get_all(self):
        return self.client.get("/campaigns")

    def get(self, campaign_id):
        return self.client.get("/campaigns/%i" % campaign_id)

    def update(self, campaign):
        return self.client.put(get_link(campaign, "update"), campaign)

    def delete(self, campaign):
        return self.client.delete(get_link(campaign, "self"))

    # copy a campaign
    def copy(self, campaign):
        return self.client.post(get_link(campaign, "copy"))

    # manage campaign's state
    def publish(self, campaign):
        return self.client.post(get_link(campaign, "publish"))

    def cancel(self, campaign):
        return self.client.post(get_link(campaign, "cancel"))

    def pause(self, campaign):
        return self.client.post(get_link(campaign, "pause"))

    def cont(self, campaign):
        return self.client.post(get_link(campaign, "continue"))

    # manage campaign's jobs
    def add_jobs(self, campaign, jobs):
        return self.client.post(get_link(campaign, "jobs"), self.get_ids(jobs))

    def update_jobs(self, campaign, jobs):
        return self.client.put(get_link(campaign, "jobs"), self.get_ids(jobs))

    def remove_jobs(self, campaign, jobs):
        return self.client.delete(get_link(campaign, "jobs"), self.get_ids(jobs))
