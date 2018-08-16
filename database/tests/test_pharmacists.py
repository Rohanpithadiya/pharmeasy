import unittest
from database.pharmacists import pharmacists
class Test_pharmacists(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_get_pharmacists_pass(self):
        pharmacist_id = 1
        expected = [{'org_name': 'Imperdiet Ullamcorper Industries', 'id': 1L, 'license': 'FDD78F6C-5E8C-C35A-6631-DF463419D2C8', 'address': '3127 Et Rd.'}]
        actual = pharmacists().get_pharmacists(pharmacist_id=pharmacist_id)
        self.assertEqual(actual,expected)

