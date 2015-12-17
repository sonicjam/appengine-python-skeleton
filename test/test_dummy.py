import unittest


class DummyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sample1(self):
        self.assertTrue(True, 'True is True')
        self.assertFalse(False, 'True is True')

    def test_sample2(self):
        self.assertEqual(True, True, 'True is True')

if __name__ == '__main__':
    unittest.main()
