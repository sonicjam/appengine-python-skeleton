import unittest

from google.appengine.api import urlfetch
from google.appengine.ext import testbed


class DummyURLFetch(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_urlfetch_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_get_request(self):
        result = urlfetch.fetch(url='http://example.com/', method=urlfetch.GET)
        self.assertEqual(200, result.status_code)
        self.assertIsNotNone(result.content)

if __name__ == '__main__':
    unittest.main()
