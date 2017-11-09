from .utils.hal import get_link


class BaseService:
    def __init__(self, client):
        self.client = client

    @staticmethod
    def get_ids(resources):
        return map(lambda r: r["id"], resources)


class CrudService(BaseService):
    # crud
    def create(self, resource):
        return self.client.post("/%s" % self.path, resource)

    def get_all(self):
        return self.client.get("/%s" % self.path)

    def get(self, resource_id):
        return self.client.get("/%s/%i" % (self.path, resource_id))

    def update(self, resource):
        return self.client.put(get_link(resource, "update"), resource)

    def delete(self, resource):
        return self.client.delete(get_link(resource, "self"))
