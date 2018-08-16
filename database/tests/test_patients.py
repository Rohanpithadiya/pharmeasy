import unittest
from database.patients import patients


class Test_patients(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_get_patients_pass(self):
        patient_id = 1
        expected = [{'dob': 1503447303L, 'mr_permission': None, 'addresss': 'Lowell', 'id': 1L, 'name': 'Rinah'}]
        actual = patients().get_patients(patient_id=patient_id)
        self.assertEqual(actual,expected)

