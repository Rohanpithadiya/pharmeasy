config = {}

server = {
    "host":"localhost",
    "port":5000,
    "endpoints":{
        "requests" : "requests/",
        "grants" : "grants/",
        "prescriptions" : "prescriptions/",
        "documents" : "documents/",
        "meta":"meta/"
    }
}

db ={
    "uri" : "postgresql://postgres:postgres@localhost/pharmeasy_db"
}

config["server"] = server
config["db"] = db