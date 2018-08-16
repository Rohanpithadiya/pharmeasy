import json
import requests
import unittest
import logging

from flask_api import status
import utils.constants as cn
from utils.config import config


class Integration_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        endpoint_url = " http://"+config["server"]["host"]+":"+str(config["server"]["port"])+"/" + "remove_grants/1"
        data = {"requester_id": 1, "req_type": cn.DOCTOR, "prescription_id": 1}
        res = requests.post(url=endpoint_url, data=data)
        print res

    @classmethod
    def tearDownClass(self):
        endpoint_url = " http://"+config["server"]["host"]+":"+str(config["server"]["port"])+"/" + "remove_grants/1"
        data = {"requester_id": 1, "req_type": cn.DOCTOR, "prescription_id": 1}
        res = requests.post(url=endpoint_url, data=data)
        print res

    def test_pass(self):
        try:
            self.init()

            # doctor 1 request for prescription from patient 1
            endpoint_url = self.server_url+config["server"]["endpoints"]["requests"]+self.doc_1
            data = {"patient_id":self.patient_1,"req_type": cn.DOCTOR,"doc_type":cn.PRESCRIPTION}
            res = requests.post(url=endpoint_url, data=data)
            self.assertEqual(res.status_code,status.HTTP_201_CREATED)

            # doctor 2 request for prescription from patient 1
            endpoint_url = self.server_url+config["server"]["endpoints"]["requests"]+self.doc_2
            data = {"patient_id":self.patient_1,"req_type": cn.DOCTOR,"doc_type":cn.PRESCRIPTION}
            res = requests.post(url=endpoint_url, data=data)
            self.assertEqual(res.status_code,status.HTTP_201_CREATED)

            # pharmacist 1 request for prescription from patient 1
            endpoint_url = self.server_url+config["server"]["endpoints"]["requests"]+self.pharma_1
            data = {"patient_id":self.patient_1,"req_type": cn.PHARMA,"doc_type":cn.PRESCRIPTION}
            res = requests.post(url=endpoint_url, data=data)
            self.assertEqual(res.status_code,status.HTTP_201_CREATED)

            # patient 1 as for all pending requests for prescriptions
            endpoint_url = self.server_url+config["server"]["endpoints"]["requests"]+self.patient_1
            params = {}
            res = requests.get(url=endpoint_url, params=params)
            self.assertEqual(res.status_code,status.HTTP_200_OK)
            all_requests = json.loads(res.content)
            # print all_requests

            # get all prescriptions for patients 1
            endpoint_url = self.server_url + config["server"]["endpoints"]["prescriptions"] + self.patient_1
            params = {}
            res = requests.get(url=endpoint_url, params=params)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            all_prescriptions = json.loads(res.content)
            # print all_prescriptions
            # convert all prescription into schama formated datastructure
            # for all_requests for patient 1
            #   select random prescription and grant to requestee

            # patient 1 Approves doctor 1 with prescription 1
            endpoint_url = self.server_url + config["server"]["endpoints"]["grants"] + self.patient_1
            data = {"requester_id":self.doc_1,"prescription_id":self.prescription_1,"req_type":cn.DOCTOR,"doc_type":cn.PRESCRIPTION}
            res = requests.post(url=endpoint_url, data=data)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

            # patient 1 reject doctor 2
            endpoint_url = self.server_url + config["server"]["endpoints"]["grants"] + self.patient_1
            data = {"requester_id":self.doc_2,"req_type":cn.DOCTOR,"doc_type":cn.PRESCRIPTION}
            res = requests.delete(url=endpoint_url, data=data)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

            # doctor1 retrives prescriptions from patient1
            endpoint_url = self.server_url + config["server"]["endpoints"]["documents"] + self.doc_1
            params = {"patient_id":self.patient_1,"req_type":cn.DOCTOR}
            res = requests.get(url=endpoint_url, params=params)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            doc_pat_prescriptions = json.loads(res.content)
            # print doc_pat_prescriptions

            # doctor 1 retrives prescription1
            endpoint_url = self.server_url + config["server"]["endpoints"]["meta"] + self.prescription_1
            params = {"requester_id":self.doc_1}
            res = requests.get(url=endpoint_url, params=params)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            prescription_detail = json.loads(res.content)
            # print prescription_detail

        except BaseException as cex:
            logging.error(cex.message)
            self.assertEqual(cex.message,"")

    def init(self):
        self.doc_1 = "1"
        self.doc_2 = "2"
        self.doc_3 = "3"

        self.pharma_1 = "1"
        self.pharma_2 = "2"
        self.pharma_3 = "3"

        self.patient_1 = "1"
        self.patient_2 = "2"
        self.patient_3 = "3"

        self.prescription_1 = "1"
        self.prescription_2 = "2"
        self.prescription_3 = "3"

        self.server_url = " http://"+config["server"]["host"]+":"+str(config["server"]["port"])+"/"
