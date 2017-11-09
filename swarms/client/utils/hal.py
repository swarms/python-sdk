from .exceptions import HalLinkNotFound


def has_link(resource, link_name):
    try:
        resource["_links"][link_name]["href"]
        return True
    except KeyError:
        return False


def get_link(resource, link_name):
    try:
        return resource["_links"][link_name]["href"]
    except KeyError:
        raise HalLinkNotFound
