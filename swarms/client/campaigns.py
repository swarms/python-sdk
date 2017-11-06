from .hal import get_link


def create(client, campaign):
    return client.post("/campaigns", campaign)


def get_all(client):
    return client.get("/campaigns")


def get(client, campaign_id):
    return client.get("/campaigns/%i" % campaign_id)


def update(client, campaign):
    return client.put(get_link(campaign, "update"), campaign)


def delete(client, campaign):
    return client.delete(get_link(campaign, "self"))


def copy(client, campaign):
    return client.post(get_link(campaign, "copy"))


def publish(client, campaign):
    return client.post(get_link(campaign, "publish"))


def cancel(client, campaign):
    return client.post(get_link(campaign, "cancel"))


def pause(client, campaign):
    return client.post(get_link(campaign, "pause"))


def cont(client, campaign):
    return client.post(get_link(campaign, "continue"))
