import unittest
import simplejson
import requests

from datetime import datetime

headers = {'content-type': 'application/json'}


class PieParse(unittest.TestCase):
    def check_eval(self, codes, expected):
        data = simplejson.dumps({'code': codes})
        r = requests.post('http://localhost:8000/v1/python/2.7.1',
                data=data,
                headers=headers)
        self.assertEquals(200, r.status_code)
        data = simplejson.loads(r.content)
        self.assertIn(expected, data['results'])

    def test_homepage(self):
        r = requests.get('http://localhost:8000/')
        self.assertEquals(200, r.status_code)


    def test_code(self):
        self.check_eval(
            'print 1+1',
            '2'
        )

    def test_timeout(self):
        early = datetime.now()

        data = simplejson.dumps({'code': 'while True:\n    print "hey!"'})
        r = requests.post('http://localhost:8000/v1/python/2.7.1', data=data, headers=headers)
        self.assertEquals(200, r.status_code)

        lenth = datetime.now() - early
        self.assertTrue(6 > lenth.seconds)

    def test_exception(self):
        self.check_eval(
            'raise Exception("hello!")',
            'Exception: hello!'
        )

    def test_syntax_error(self):
        self.check_eval(
            'for x in range(10)\n    print "hey!"',
            'SyntaxError: invalid syntax (<string>, line 1)'
        )

    def test_restricted_error(self):
        self.check_eval(
            'f = open("/etc/secret", "r")',
            "IOError: [Errno 13]"
        )


if __name__ == '__main__':
    unittest.main()
