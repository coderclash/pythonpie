import unittest
import pythonpie
import simplejson

from datetime import datetime


class PieParse(unittest.TestCase):
    def setUp(self):
        pythonpie.app.config['TESTING'] = True
        self.app = pythonpie.app.test_client()

    def check_eval(self, codes, expected):
        data = simplejson.dumps({'code': codes})
        rv = self.app.post('/v1/python/2.7.1', data=data, content_type='application/json')
        self.assertEquals(200, rv.status_code)
        data = simplejson.loads(rv.data)
        self.assertEquals(data['results'], expected)

    def test_homepage(self):
        rv = self.app.get('/')
        self.assertEquals(200, rv.status_code)

    def test_code(self):
        self.check_eval(
            'print 1+1',
            '2'
        )

    def test_timeout(self):
        early = datetime.now()

        data = simplejson.dumps({'code': 'while True: print "hey!"'})
        rv = self.app.post('/v1/python/2.7.1', data=data, content_type='application/json')
        self.assertEquals(200, rv.status_code)

        lenth = datetime.now() - early
        self.assertTrue(5 < lenth)


if __name__ == '__main__':
    unittest.main()
