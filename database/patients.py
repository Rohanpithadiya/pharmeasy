from database.db_connection import get_connection
from database.schemas import schema,serializer
from utils.logger import serviceLogger as logging


class patients:
    def __init__(self):
        self.conn = get_connection()

    def __del__(self):
        self.conn.commit()

    def get_patients(self, patient_id):
        query = "select * from patients where " \
                "id = " + str(patient_id) + \
                ";"
        cur = self.conn.cursor()
        cur.execute(query)
        list = cur.fetchall()
        data = serializer(data=list, table_schema=schema["patients"])
        logging.info("served patient by its id")
        return data
