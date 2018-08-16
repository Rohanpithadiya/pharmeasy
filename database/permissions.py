from database.db_connection import get_connection
from database.schemas import schema,serializer
from utils.logger import serviceLogger as logging

class permissions:
    def __init__(self):
        self.conn = get_connection()

    def __del__(self):
        self.conn.commit()


    def grant_request(self,requester_id, patient_id, prescription_id, req_type):
        query = "insert into permissions (requester_id, patient_id, prescription_id,requester_type) " \
                "values ('" + str(requester_id) + \
                "','" + str(patient_id) + \
                "','" + str(prescription_id) + \
                "','" + req_type + \
                "');"
        cur = self.conn.cursor()
        cur.execute(query)
        logging.info(" Insert permission request into DB")
        return True

    def get_prescriptions(self,requester_id, patient_id, requester_type):
        query = "select * from permissions where " \
                "requester_id = " + str(requester_id) + \
                " and patient_id = " + str(patient_id) + \
                " and requester_type = '" + str(requester_type) + \
                "';"
        cur = self.conn.cursor()
        cur.execute(query)
        list = cur.fetchall()
        data = serializer(data=list,schema=schema["permissions"])
        logging.info(" served prescription to doctors about patients")
        return data

    def is_permitted(self,prescription_id,requester_id):
        try:
            query = "select * from permissions where " \
                    "prescription_id = " + str(prescription_id) + \
                    " and requester_id = " + str(requester_id) + \
                    ";"
            cur = self.conn.cursor()
            cur.execute(query)
            list = cur.fetchall()
            if(len(list)):
                return True
            else:
                return False
        except:
            return False

    def remove_permission(self, requester_id, patient_id, prescription_id, req_type):
        query = "delete from permissions where " \
                "requester_id = '" + str(requester_id) + \
                "'and patient_id = '" + str(patient_id) + \
                "'and prescription_id = '" + str(prescription_id) + \
                "'and requester_type = '" + req_type + \
                "';"
        cur = self.conn.cursor()
        cur.execute(query)
        logging.info(" delete permission request into DB")
        return True
