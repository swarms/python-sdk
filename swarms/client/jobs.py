from .utils.hal import get_link
from . import BaseService


class Jobs(BaseService):
    def __init__(self, client):
        self.client = client

    # crud
    def create(self, job):
        return self.client.post("/jobs", job)

    def get_all(self):
        return self.client.get("/jobs")

    def get(self, job_id):
        return self.client.get("/jobs/%i" % job_id)

    def update(self, job):
        return self.client.put(get_link(job, "update"), job)

    def delete(self, job):
        return self.client.delete(get_link(job, "self"))

    # copy a job
    def copy(self, job):
        return self.client.post(get_link(job, "copy"))
