import unittest
from database.permissions import permissions
import utils.constants as cn
from database.tests.setup_db import insert_permission_into_db


class Test_permissions(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        insert_permission_into_db()
        pass

    @classmethod
    def tearDownClass(self):
        patient_id = 4
        requester_id = 4
        prescription_id = 2
        req_type = cn.DOCTOR
        permissions().remove_permission(requester_id=requester_id,
                                             patient_id=patient_id,
                                             prescription_id=prescription_id,
                                             req_type=req_type)


    def test_grant_request_pass(self):
        patient_id = 4
        requester_id = 4
        prescription_id = 2
        req_type = cn.DOCTOR
        expected = True
        actual = permissions().grant_request(requester_id=requester_id,
                                             patient_id=patient_id,
                                             prescription_id=prescription_id,
                                             req_type=req_type)
        self.assertEqual(actual,expected)

    def test_get_prescriptions_pass(self):
        patient_id = 1
        requester_id = 1
        requester_type = cn.DOCTOR
        expected = [{'ttl': None, 'requester_id': 1L, 'prescription_id': 1L, 'requester_type': 'DR', 'patient_id': 1L}]
        actual = permissions().get_prescriptions(requester_id=requester_id,
                                                 patient_id=patient_id,
                                                 requester_type=requester_type)
        self.assertEqual(actual,expected)

    def test_is_permitted_pass(self):
        prescription_id = 2
        requester_id = 4
        expected = True
        actual = permissions().is_permitted(prescription_id=prescription_id,requester_id=requester_id)
        self.assertEqual(actual,expected)

