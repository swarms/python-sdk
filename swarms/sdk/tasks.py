import requests
from .utils.hal import get_link
from . import CrudService
import os.path
import magic


class Tasks(CrudService, object):
    path = "tasks"

    def __upload_from_url(self, url):
        if os.path.isfile(url):
            file_name = url
            f = open(file_name, 'rb')
            mime = magic.Magic(mime=True)
            mimetype = mime.from_file(file_name)

        else:
            file_name = url.split('/')[-1]
            response = requests.get(url)

            if response.status_code != 200:
                raise Exception("Could not retrieve file: %s" % url)

            mimetype = response.headers['Content-Type']

            f = response.content

        return self.client.post_file("/upload", file_name, f, mimetype)

    def __get_url_map(self, components):
        urls = [c["url"] for c in components if "url" in c.keys()]
        url_map = {}

        for url in urls:
            url_map[url] = self.__upload_from_url(url)

        return url_map

    def create(self, resource):
        url_map = self.__get_url_map(resource["components"])

        for component in resource["components"]:
            if "url" in component.keys():
                component["url"] = url_map[component["url"]]

        return super(Tasks, self).create(resource)

    # copy a task
    def copy(self, task):
        return self.client.post(get_link(task, "copy"))
