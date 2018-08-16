from database.db_connection import get_connection


def insert_permission_into_db():
    conn = get_connection()
    query = "insert into permissions(patient_id,requester_id,prescription_id,requester_type) values (1,1,1,'DR');"
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
