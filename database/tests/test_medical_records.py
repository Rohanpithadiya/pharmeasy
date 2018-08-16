import unittest
from database.medical_records import medical_records


class Test_medical_records(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_prescriptions_by_patient_id_pass(self):
        patient_id = 1
        expected = [{'doctor_id': 1, 'prescription_id': 1, 'updated_at': 1534188919000, 'patient_id': 1},
                    {'doctor_id': 2, 'prescription_id': 2, 'updated_at': 1534188919000, 'patient_id': 1}]
        actual = medical_records().prescriptions_by_patient_id(patient_id=patient_id)
        self.assertEqual(actual,expected)
