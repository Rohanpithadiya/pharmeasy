from database.db_connection import get_connection
def setup_db():
    conn = get_connection()
    cur = conn.cursor()

    query = "insert into prescriptions(type, meta) values('text','abc 50mg, xyx.10mg, etc..')"
    cur.execute(query)

    query = "insert into prescriptions(type, meta) values('image','http://somes3url')"
    cur.execute(query)

    query = "insert into pharmacists (id, org_name, licence, address) values('image','http://somes3url')"
    cur.execute(query)


    conn.commit()