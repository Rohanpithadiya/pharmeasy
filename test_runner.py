import unittest

from tests.intigration_tests import Integration_test
from database.tests.test_db_connection import Test_db_connection
from database.tests.test_schema import Test_schema
from database.tests.test_doctors import Test_doctors
from database.tests.test_patients import Test_patients
from database.tests.test_pharmacists import Test_pharmacists
from database.tests.test_medical_records import Test_medical_records
from database.tests.test_permissions import Test_permissions
from database.tests.test_permissions_requests import Test_permissions_requests
from database.tests.test_prescriptions import Test_prescriptions
if __name__ == '__main__':
    unittest.main()