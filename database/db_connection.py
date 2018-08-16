import psycopg2

from utils.config import db
import utils.messages as msg

conn = None
def get_connection():
    global conn

    if conn != None:
        # print "its working"
        return  conn
    else:
        try:
            # conn = psycopg2.connect("dbname='pharmEasy_db' user='postgres' host='localhost' password='postgres'")
            conn = psycopg2.connect(db["uri"])
        except:
            print msg.DB_CONNECTION_ERROR
            raise
    return conn
