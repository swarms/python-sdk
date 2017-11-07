from .hal import get_link


# crud
def create(client, job):
    return client.post("/jobs", job)


def get_all(client):
    return client.get("/jobs")


def get(client, job_id):
    return client.get("/jobs/%i" % job_id)


def update(client, job):
    return client.put(get_link(job, "update"), job)


def delete(client, job):
    return client.delete(get_link(job, "self"))


# copy a job
def copy(client, job):
    return client.post(get_link(job, "copy"))
