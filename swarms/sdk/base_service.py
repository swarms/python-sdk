from .utils.hal import has_link, get_link


class BaseService:
    def __init__(self, client):
        self.client = client

    @staticmethod
    def get_ids(resources):
        return list(map(lambda r: r["id"], resources))


class CrudService(BaseService):
    # crud
    def create(self, resource):
        return self.client.post("/%s" % self.path, resource)

    def get_all(self):
        page = None
        all_list = []

        while True:
            page = self.next_page(page)

            if page is None:
                return all_list

            all_list.extend(page[self.path])

    def get_page(self):
        return self.next_page()

    def next_page(self, collection=None):
        if collection is None:
            return self.client.get("/%s" % self.path)
        elif has_link(collection, "next"):
            return self.client.get(get_link(collection, "next"))

    def get(self, resource_id):
        return self.client.get("/%s/%i" % (self.path, resource_id))

    def update(self, resource):
        return self.client.put(get_link(resource, "self"), resource)

    def delete(self, resource):
        return self.client.delete(get_link(resource, "self"))
