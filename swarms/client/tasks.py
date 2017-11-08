from .utils.hal import get_link
from . import CrudService


class Tasks(CrudService):
    path = "tasks"

    # copy a task
    def copy(self, task):
        return self.client.post(get_link(task, "copy"))
