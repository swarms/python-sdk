from .utils.hal import has_link, get_link
from . import CrudService


class Campaigns(CrudService):
    path = "campaigns"

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
    def get_jobs(self, campaign):
        return self.client.get(get_link(campaign, "jobs"))

    def add_jobs(self, campaign, jobs):
        return self.client.post(get_link(campaign, "jobs"), self.get_ids(jobs))

    def update_jobs(self, campaign, jobs):
        return self.client.put(get_link(campaign, "jobs"), self.get_ids(jobs))

    def remove_jobs(self, campaign, jobs):
        return self.client.delete(get_link(campaign, "jobs"), self.get_ids(jobs))

    # get campaign's results
    def results(self, campaign):
        if has_link(campaign, "results"):
            return self.client.get(get_link(campaign, "results"))
        else:
            return {"jobResults": []}
