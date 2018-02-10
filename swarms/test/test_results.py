import unittest
from ..sdk import Client, Results
from . import config


class ResultsTest(unittest.TestCase):
    client = Client(config.base_url, config.username, config.password)
    results = Results(client)

    def test_approve(self):
        self.results.approve({
            "_links": {
                "approve": {
                    "href": "/results/3/approve"
                }
            }
        })

    def test_reject(self):
        self.results.reject({
            "_links": {
                "reject": {
                    "href": "/results/3/reject"
                }
            }
        })

    def test_soft_reject(self):
        self.results.soft_reject({
            "_links": {
                "softReject": {
                    "href": "/results/3/soft-reject"
                }
            }
        })


if __name__ == '__main__':
    unittest.main()
