import unittest
from database.schemas import serializer,schema

class Test_schema(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_serializer_pass(self):
        expected = [
            {"patient_id": 1,
             "requester_id": 1,
             "requester_type": "DR",
             "doc_type": "PR"
             },
            {"patient_id": 1,
             "requester_id": 2,
             "requester_type": "DR",
             "doc_type": "PR"
             },
            {"patient_id": 1,
             "requester_id": 1,
             "requester_type": "PH",
             "doc_type": "PR"
             },
        ]

        data = [[1, 1, u'DR', u'PR'], [1, 2, u'DR', u'PR'], [1, 1, u'PH', u'PR']]
        actual = serializer(data=data, schema=schema["permission_requests"])
        self.assertEqual(actual, expected)