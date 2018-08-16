from database.db_connection import get_connection
def clear_db():
    conn = get_connection()


    query = "delete from permission_requests;"
    cur = conn.cursor()
    cur.execute(query)

    query = "delete from doctors;"
    cur = conn.cursor()
    cur.execute(query)

    query = "delete from medical_records;"
    cur = conn.cursor()
    cur.execute(query)

    query = "delete from patients;"
    cur = conn.cursor()
    cur.execute(query)

    query = "delete from pharmacists;"
    cur = conn.cursor()
    cur.execute(query)

    query = "delete from prescriptions;"
    cur = conn.cursor()
    cur.execute(query)

    query = "delete from permissions;"
    cur = conn.cursor()
    cur.execute(query)

    conn.commit()
