import json
from flask_api import status
from flask import Response
import utils.constants as cn
from database.medical_records import medical_records
from database.permissions import permissions
from database.prescriptions import prescriptions

def get(patient_id):
    list = medical_records().prescriptions_by_patient_id(patient_id=patient_id)
    return Response(response=json.dumps(list),status=status.HTTP_200_OK)

def get_detail(prescription_id,requester_id):
    if permissions().is_permitted(prescription_id,requester_id):
        details = prescriptions().get_prescription(prescription_id=prescription_id)
        return Response(response=json.dumps(details),status=status.HTTP_200_OK)
    else:
        Response(response={},status=status.HTTP_403_FORBIDDEN)