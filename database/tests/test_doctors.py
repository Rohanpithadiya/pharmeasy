import unittest
from database.doctors import doctors
class Test_doctors(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_get_doctors_pass(self):
        doctor_id = 1
        expected = [{'org': 'Dictum Eu Eleifend Inc.', 'qualifications': 'MBBS', 'id': 1, 'name': 'Umaprasad'}]
        actual = doctors().get_doctors(doctor_id=doctor_id)
        self.assertEqual(actual,expected)

