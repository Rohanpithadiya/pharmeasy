from database.db_connection import get_connection
from database.schemas import schema,serializer
from utils.logger import serviceLogger as logging

class medical_records:
    def __init__(self):
        self.conn = get_connection()

    def __del__(self):
        self.conn.commit()


    def prescriptions_by_patient_id(self, patient_id):

        query = "select * from medical_records where " \
                "patient_id = " + str(patient_id) + \
                ";"
        cur = self.conn.cursor()
        cur.execute(query)
        list = cur.fetchall()
        data = serializer(data=list, table_schema=schema["medical_records"])
        logging.info("served all medical_records of given patient")
        return data
