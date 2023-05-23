import pytest
import json
import unittest
import sys, os
sys.path.append('../')

import app

class Test(unittest.TestCase):

    def test_index(self):
        
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200, "Status should be 200.")

if __name__ == '__main__':
    unittest.main()
