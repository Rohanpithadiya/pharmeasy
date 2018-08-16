import json

doctors = [("id","int"),("name","str"),("org","str"),("qualifications","str")]
pharmacists = [("id","int"),("org_name","str"),("license","str"),("address","str")]
patients = [("id","int"),("name","str"),("dob","int"),("addresss","str"),("mr_permission","json")]
medical_records = [("patient_id","int"),("doctor_id","int"),("prescription_id","int"),("updated_at","int")]
prescriptions = [("id","int"),("type","str"),("meta","str")]
permissions = [("patient_id","int"),("requester_id","int"),("prescription_id","int"),("requester_type","str"),("ttl","int")]
permission_requests = [("patient_id","int"),("requester_id","int"),("requester_type","str"),("doc_type","str")]

schema = {
    "doctors":doctors,
    "pharmacists":pharmacists,
    "patients":patients,
    "medical_records":medical_records,
    "prescriptions":prescriptions,
    "permissions":permissions,
    "permission_requests":permission_requests
}

def serializer(data, schema):
    res = []
    if type(data) != list:
        data = [data]
    for row in data:
        element = {}
        for i in range(0,len(row)):
            # if row[i]:
                element[schema[i][0]] = row[i]
            # else:
            #     element[schema[i][0]] = None
        res.append(element)
    return res

