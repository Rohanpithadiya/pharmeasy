import unittest
from database.db_connection import get_connection

class Test_db_connection(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_get_connection_pass(self):
        expected = None
        result = get_connection()
        self.assertNotEqual(expected,result)
