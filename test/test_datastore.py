import unittest

from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed


class DummyModel(ndb.Model):
    number = ndb.IntegerProperty(default=42)
    text = ndb.StringProperty()


class DummyEntityGroupRoot(ndb.Model):
    pass


def get_entity_via_memcache(entity_key):
    entity = memcache.get(entity_key)
    if entity is not None:
        return entity
    key = ndb.Key(urlsafe=entity_key)
    entity = key.get()
    if entity is not None:
        memcache.set(entity_key, entity)
    return entity


class DummyDatastore(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def test_insert_entity(self):
        DummyModel().put()
        self.assertEqual(1, len(DummyModel.query().fetch(2)))

if __name__ == '__main__':
    unittest.main()
