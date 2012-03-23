import unittest
import pythonpie


class PieParse(unittest.TestCase):
    def setUp(self):
        pythonpie.app.config['TESTING'] = True
        self.app = pythonpie.app.test_client()

    def test_homepage(self):
        rv = self.app.get('/')
        self.assertEquals(200, rv.status_code)


if __name__ == '__main__':
    unittest.main()
