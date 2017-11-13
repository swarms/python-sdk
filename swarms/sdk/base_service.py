from .utils.hal import has_link, get_link


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
        list = None
        all = []

        while True:
            list = self.next_page(list)

            if list is None:
                return all

            all.extend(list)

    def get_page(self):
        return self.next_page()

    def next_page(self, collection=None):
        if collection is None:
            return self.client.get("/%s?limit=1" % self.path)
            return self.client.get("/%s" % self.path)
        elif has_link(collection, "next"):
            return self.client.get(get_link(collection, "next"))
        else:
            return None

    def get(self, resource_id):
        return self.client.get("/%s/%i" % (self.path, resource_id))

    def update(self, resource):
        return self.client.put(get_link(resource, "update"), resource)

    def delete(self, resource):
        return self.client.delete(get_link(resource, "self"))
