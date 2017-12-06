from .utils.hal import get_link
from . import CrudService


class Jobs(CrudService):
    path = "jobs"

    # copy a job
    def copy(self, job):
        return self.client.post(get_link(job, "copy"))

    # manage job's tasks
    def get_all_tasks(self, job):
        return self.get_all_from_link(get_link(job, "tasks"), "tasks")

    def get_tasks(self, job):
        return self.client.get(get_link(job, "tasks"))

    def update_tasks(self, job, tasks):
        return self.client.put(get_link(job, "tasks"), self.get_ids(tasks))
