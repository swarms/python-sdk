from .hal import get_link


# crud
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


# copy a campaign
def copy(client, campaign):
    return client.post(get_link(campaign, "copy"))


# manage campaign's state
def publish(client, campaign):
    return client.post(get_link(campaign, "publish"))


def cancel(client, campaign):
    return client.post(get_link(campaign, "cancel"))


def pause(client, campaign):
    return client.post(get_link(campaign, "pause"))


def cont(client, campaign):
    return client.post(get_link(campaign, "continue"))


def get_ids(resources):
    return map(lambda r: r["id"], resources)


# manage campaign's jobs
def add_jobs(client, campaign, jobs):
    return client.post(get_link(campaign, "jobs"), get_ids(jobs))


def update_jobs(client, campaign, jobs):
    return client.put(get_link(campaign, "jobs"), get_ids(jobs))


def remove_jobs(client, campaign, jobs):
    return client.delete(get_link(campaign, "jobs"), get_ids(jobs))
