import json

from flask_api import status
from flask import Response
import utils.constants as cn
from database.permissions_requests import permissions_requests


def post(requester_id, patient_id, req_type,doc_type):
    if (req_type in [cn.DOCTOR, cn.PHARMA]) and \
            (doc_type in [cn.MR, cn.PRESCRIPTION]):
        permissions_requests().create_request(requester_id=requester_id,
                                              patient_id=patient_id,
                                              requester_type= req_type,
                                              doc_type=doc_type)
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def get(patient_id):
    permission_list = permissions_requests().get_all_requests(patient_id=patient_id)
    return Response(response=json.dumps(permission_list),status=status.HTTP_200_OK)
