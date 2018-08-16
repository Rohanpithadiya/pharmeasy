from database.db_connection import get_connection
from database.schemas import schema,serializer
from utils.logger import serviceLogger as logging


class doctors:
    def __init__(self):
        self.conn = get_connection()

    def __del__(self):
        self.conn.commit()

    def get_doctors(self,doctor_id):
        query = "select * from doctors where " \
                "id = " + str(doctor_id) + \
                ";"
        cur = self.conn.cursor()
        cur.execute(query)
        list = cur.fetchall()
        data = serializer(data=list, schema=schema["doctors"])
        logging.info("served doctor by its id")
        return data
