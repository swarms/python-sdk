from .utils.hal import has_link, get_link


class BaseService:
    def __init__(self, client):
        self.client = client

    @staticmethod
    def get_ids(resources):
        return list(map(lambda r: r["id"], resources))

    def get_all_from_link(self, link, path):
        page = self.client.get(link)
        all_list = []

        while True:
            all_list.extend(page[path])
            page = self.next_page(path, page)

            if page is None:
                return all_list

    def next_page(self, path, collection=None):
        if has_link(collection, "next"):
            return self.client.get(get_link(collection, "next"))


class CrudService(BaseService):
    # crud
    def create(self, resource):
        return self.client.post("/%s" % self.path, resource)

    def get_all(self):
        return self.get_all_from_link("/%s" % self.path, self.path)

    def get_page(self):
        return self.client.get("/%s" % self.path)

    def get(self, resource_id):
        return self.client.get("/%s/%i" % (self.path, resource_id))

    def update(self, resource):
        return self.client.put(get_link(resource, "self"), resource)

    def delete(self, resource):
        return self.client.delete(get_link(resource, "self"))
