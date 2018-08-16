from database.db_connection import get_connection
from utils.logger import serviceLogger as logging

from database.schemas import serializer,schema


class permissions_requests:
    def __init__(self):
        self.conn = get_connection()

    def __del__(self):
        self.conn.commit()

    def create_request(self, requester_id, patient_id, requester_type, doc_type):
        try:
            query = "insert into permission_requests (requester_id, patient_id, requester_type, doc_type) " \
                    "values ('" + str(requester_id) + \
                    "','" + str(patient_id) + \
                    "','" + requester_type + \
                    "','" + doc_type + \
                    "');"
            cur = self.conn.cursor()
            cur.execute(query)
            logging.info(" Insert permission request into DB")
            return True
        except BaseException as bex:
            logging.error(bex.message)
            return False

    def get_all_requests(self, patient_id):
        query = "select * from permission_requests where " \
                "patient_id = " + str(patient_id) + \
                ";"
        cur = self.conn.cursor()
        cur.execute(query)
        list = cur.fetchall()
        data = serializer(data=list,schema=schema["medical_records"])
        logging.info(" served all requests for patient")
        return data

    def remove_requests(self,requester_id,patient_id,req_type, doc_type):
        try:
            query = "delete from permission_requests where requester_id ='" + str(requester_id) + \
                    "'and patient_id ='" + str(patient_id) + \
                    "'and requester_type = '" + req_type + \
                    "'and doc_type = '" + doc_type + \
                    "';"
            cur = self.conn.cursor()
            cur.execute(query)
            logging.info(" remove permission request from DB")
            return True
        except BaseException as bex:
            logging.error(bex.message)
            return False
