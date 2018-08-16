from database.db_connection import get_connection
from database.schemas import schema,serializer
from utils.logger import serviceLogger as logging


class pharmacists:
    def __init__(self):
        self.conn = get_connection()

    def __del__(self):
        self.conn.commit()

    def get_pharmacists(self,pharmacist_id):
        query = "select * from pharmacists where " \
                "id = " + str(pharmacist_id) + \
                ";"
        cur = self.conn.cursor()
        cur.execute(query)
        list = cur.fetchall()
        data = serializer(data=list, table_schema=schema["pharmacists"])
        logging.info("served pharmacist by its id")
        return data
