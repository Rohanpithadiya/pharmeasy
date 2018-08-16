import json

from flask_api import status
from flask import Response
import utils.constants as cn
from database.permissions import permissions


def get(requester_id, patient_id, req_type):
    permission_list = permissions().get_prescriptions(requester_id =requester_id, patient_id=patient_id,requester_type = req_type)
    if req_type in [cn.DOCTOR,cn.PHARMA]:
        return Response(response=json.dumps(permission_list),status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
