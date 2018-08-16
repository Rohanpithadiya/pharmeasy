from database.db_connection import get_connection
from utils.logger import serviceLogger as logging
from database.schemas import schema,serializer

class prescriptions:
    def __init__(self):
        self.conn = get_connection()

    def __del__(self):
        self.conn.commit()


    def get_prescription(self,prescription_id):
        query = "select * from prescriptions where " \
                "id = " + str(prescription_id) +\
                ";"
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        details = serializer(data=rows, table_schema=schema["prescriptions"])
        logging.info("retrived prescriptions from id")
        return details