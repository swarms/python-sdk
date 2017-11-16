import unittest
from ..sdk import Client, Jobs
from . import config


class JobsTest(unittest.TestCase):
    client = Client(config.base_url, config.username, config.password)
    jobs = Jobs(client)

    def test_jobs_create(self):
        self.jobs.create({"name": "My zen job"})

    def test_jobs_get_page(self):
        page = self.jobs.get_page()
        self.assertEqual(page["jobs"][0]["name"], "My first Job")

    def test_jobs_get_one(self):
        job = self.jobs.get(3)
        self.assertEqual(job["name"], "My first Job")

    def test_jobs_update(self):
        job = self.jobs.update({
            "name": "My zen job",
            "title": "Zen job",
            "_links": {
                "self": {
                    "href": "/jobs/3"
                }
            }
        })
        self.assertEqual(job["name"], "My first Job")

    def test_jobs_delete(self):
        self.jobs.delete({
            "_links": {
                "self": {
                    "href": "/jobs/3"
                }
            }
        })

    def test_jobs_copy(self):
        job = self.jobs.copy({
            "_links": {
                "copy": {
                    "href": "/jobs/3/copy"
                }
            }
        })
        self.assertEqual(job["name"], "My first Job")

    def test_get_job_tasks(self):
        tasks = self.jobs.get_tasks({
            "_links": {
                "tasks": {
                    "href": "/jobs/3/tasks"
                }
            }
        })
        self.assertEqual(tasks["tasks"][0]["name"], "My first Task")

    def test_update_job_tasks(self):
        self.jobs.update_tasks({
            "_links": {
                "tasks": {
                    "href": "/jobs/3/tasks"
                }
            }
        }, [{"id": 1}, {"id": 2}, {"id": 3}])


if __name__ == '__main__':
    unittest.main()
