import unittest
from database.prescriptions import prescriptions


class Test_prescriptions(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_get_prescriptions_by_id_pass(self):
        prescription_id = 1
        expected = [{'meta': 'abc 50mg, xyx.10mg, etc..', 'type': 'text', 'id': 1L}]
        actual = prescriptions().get_prescription(prescription_id=prescription_id)
        self.assertEqual(actual,expected)

