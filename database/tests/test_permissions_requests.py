import unittest
from database.permissions_requests import permissions_requests
import utils.constants as cn


class Test_permissions_requests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_create_request_pass(self):
        patient_id = 4
        requester_id = 4
        req_type = cn.DOCTOR
        doc_type = cn.PRESCRIPTION
        expected = True
        actual = permissions_requests().create_request(requester_id=requester_id,
                                                       patient_id=patient_id,
                                                       doc_type =doc_type,
                                                       requester_type=req_type)
        self.assertEqual(actual,expected)

    def test_get_all_requests_pass(self):
        patient_id = 1
        requester_id = 1
        requester_type = cn.DOCTOR
        expected = {'doctor_id': 1L, 'prescription_id': 'DR', 'updated_at': 'PR', 'patient_id': 1L}
        actual = permissions_requests().get_all_requests(patient_id=patient_id)
        self.assertEqual(actual[0],expected)

    def test_remove_requests_pass(self):
        patient_id = 4
        requester_id = 4
        req_type = cn.DOCTOR
        doc_type = cn.PRESCRIPTION
        expected = True
        actual = permissions_requests().remove_requests(requester_id=requester_id,
                                                        patient_id=patient_id,
                                                        doc_type =doc_type,
                                                        req_type=req_type)
        self.assertEqual(actual,expected)

