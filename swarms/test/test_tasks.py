import unittest
from ..sdk import Client, Tasks
from . import config


class TasksTest(unittest.TestCase):
    client = Client(config.base_url, config.username, config.password)
    tasks = Tasks(client)

    def test_tasks_create(self):
        self.tasks.create({
            "name": "One hand clapping",
            "components": [
                {
                    "type": "Instruction",
                    "text": "Record the sound of one hand clapping.",
                }, {
                    "type": "AudioRecording",
                    "minDurationInSeconds": 3,
                    "maxDurationInSeconds": 9,
                }
            ]
        })

    def test_tasks_get_page(self):
        page = self.tasks.get_page()
        self.assertEqual(page["tasks"][0]["name"], "My first Task")

    def test_tasks_get_one(self):
        task = self.tasks.get(3)
        self.assertEqual(task["name"], "My first Task")

    def test_tasks_update(self):
        task = self.tasks.update({
            "name": "One hand clapping",
            "_links": {
                "self": {
                    "href": "/tasks/3"
                }
            }
        })
        self.assertEqual(task["name"], "My first Task")

    def test_tasks_delete(self):
        self.tasks.delete({
            "_links": {
                "self": {
                    "href": "/tasks/3"
                }
            }
        })

    def test_tasks_copy(self):
        task = self.tasks.copy({
            "_links": {
                "copy": {
                    "href": "/tasks/3/copy"
                }
            }
        })
        self.assertEqual(task["name"], "My first Task")


if __name__ == '__main__':
    unittest.main()
