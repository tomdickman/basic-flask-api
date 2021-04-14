import unittest
import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        resp = self.app.get('/tom')
        data = json.loads(resp.data)
        assert data['message'] == "Hello Tom!"
        assert resp.status_code == 200

if __name__ == '__main__':
    unittest.main()
