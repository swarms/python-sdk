from .utils.hal import get_link
from . import BaseService


class Results(BaseService):
    def approve(self, result):
        return self.client.post(get_link(result, "approve"))

    def reject(self, result):
        return self.client.post(get_link(result, "reject"))

    def soft_reject(self, result):
        return self.client.post(get_link(result, "softReject"))
