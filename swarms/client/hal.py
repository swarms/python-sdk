from .exceptions import HalLinkNotFound


def get_link(resource, link_name):
    try:
        return resource["_links"][link_name]["href"]
    except KeyError:
        raise HalLinkNotFound
