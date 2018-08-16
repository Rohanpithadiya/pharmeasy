import psycopg2

from utils.config import db
import utils.messages as msg

conn = None
def get_connection():
    global conn

    if conn != None:
        return  conn
    else:
        try:
            conn = psycopg2.connect(db["uri"])
        except:
            print msg.DB_CONNECTION_ERROR
            raise
    return conn
