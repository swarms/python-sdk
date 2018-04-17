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
    def get_all_jobs(self, campaign):
        return self.get_all_from_link(get_link(campaign, "jobs"), "jobs")

    def get_jobs(self, campaign):
        return self.client.get(get_link(campaign, "jobs"))

    def add_jobs(self, campaign, jobs):
        return self.client.post(get_link(campaign, "jobs"), self.get_ids(jobs))

    def update_jobs(self, campaign, jobs):
        return self.client.put(get_link(campaign, "jobs"), self.get_ids(jobs))

    # Not in the Apiary docs we're testing against. Plus it's weird anyway...
    #
    # def remove_jobs(self, campaign, jobs):
    #     job_ids = self.get_ids(jobs)
    #     url = get_link(campaign, "jobs") + "/" + ",".join(map(str, job_ids))
    #     print(url)
    #     return self.client.delete(url)

    # get campaign's results
    def get_all_results(self, campaign):
        if has_link(campaign, "results"):
            return self.get_all_from_link(get_link(campaign, "results"), "results")
        else:
            return []

    def get_results(self, campaign):
        if has_link(campaign, "results"):
            return self.client.get(get_link(campaign, "results"))
